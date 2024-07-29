import pygame 
from random import randint
import math 
from sklearn.cluster import KMeans

def distance(p1, p2):
	return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))

pygame.init()

running = True

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200,700))
pygame.display.set_caption("Kmeans Visualization")


# set color
bg = (214,214,214)
black = (0,0,0)
white = (255,255,255)
bgDisplay = (249,255,230)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (147,153,35)
purple = (255,0,255)
sky = (0,255,255)
orange = (255,125,25)
grape = (100,25,125)
grass = (55,155,65)

color = [red,green,blue,yellow,purple,sky,orange,grape,grass]

# font
font = pygame.font.SysFont('sans',40)
fontSmall = pygame.font.SysFont('sans',30)
text_plus = font.render('+',True,white)
text_minus = font.render('-',True,white)
text_run = font.render('Run',True,white)
text_random = font.render('Random',True,white)
text_Algorithm = font.render('Algorithm',True,white)
text_reset = font.render('Reset',True,white)
 
K = 0
Error = 0 
points = []
clusers = []
lables = []

while running:
	#draw mouse positon
	mouse_x , mouse_y = pygame.mouse.get_pos()

	clock.tick(60)
	screen.fill(bg)
	#draw interface display
	pygame.draw.rect(screen,black, (50,50,700,500))
	pygame.draw.rect(screen,bgDisplay, (53,53,694,494))
	# draw interface button
		# draw button + 
	pygame.draw.rect(screen,black, (800,50,50,50))
	screen.blit(text_plus, (815,50))
		# draw button -
	pygame.draw.rect(screen,black, (900,50,50,50))
	screen.blit(text_minus, (915,50))		
		# draw run 
	pygame.draw.rect(screen,black, (800,150,150,50))
	screen.blit(text_run, (840,150))	
		# draw random
	pygame.draw.rect(screen,black, (800,250,150,50))
	screen.blit(text_random, (815,250))	
		# draw thuật toán
	pygame.draw.rect(screen,black, (800,450,150,50))
	screen.blit(text_Algorithm, (805,450))		 
	    # draw reset 
	pygame.draw.rect(screen,black, (800,550,150,50))
	screen.blit(text_reset, (830,550))	
	
	#draw K values 
	text_K = font.render('K = ' +str(K),True,black) 
	screen.blit(text_K, (1000,50))

	# draw cusor
	if 52 < mouse_x < 747 and 52 < mouse_y < 547 :	
		text_mouse = fontSmall.render(f"({mouse_x-52}, {mouse_y-52})",True,black)	
		screen.blit(text_mouse, (mouse_x+10,mouse_y))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			# draw point when click in display 
			if 52 < mouse_x < 747 and 52 < mouse_y < 547 :	
				point = [mouse_x-52,mouse_y-52]
				points.append(point)
				print(points)
			if 800 < mouse_x < 850 and 50 < mouse_y < 100 :
				if K < 9:
					K +=1 
					print("key +")
			if 900 < mouse_x < 950 and 50 < mouse_y < 100 :
				if K > 0 :
					K -=1
					print("key -")
			if 800 < mouse_x < 950 and 150 < mouse_y < 200 :
				lables = []# reset lại ban đầu 

				if clusers == []:
					continue

				# gán những điểm vào các cluster gần nhất
				for p in points:
					distance_to_cluster = []
					for c in clusers:
						dis = distance(p,c)
						distance_to_cluster.append(dis)
					min_distance = min(distance_to_cluster)
					lable = distance_to_cluster.index(min_distance)
					lables.append(lable)
				# cập nhật cluster
				for i in range(K):
					sum_x = 0 
					sum_y = 0 
					count = 0 
					for j in range(len(points)):
						if lables[j] == i:
							sum_x += points[j][0] 
							sum_y += points[j][1]
							count += 1 
					if count != 0:
						new_cluster_x = sum_x/count
						new_cluster_y = sum_y/count	
						clusers[i] = [new_cluster_x,new_cluster_y]	

				print("key Run")
			if 800 < mouse_x < 950 and 250 < mouse_y < 300 :
				clusers = []
				lables = []
				for i in range(K):
					random_point = [randint(0,693),randint(0,493)]
					clusers.append(random_point)
					print("key Random")

			if 800 < mouse_x < 950 and 450 < mouse_y < 500 :
				try:
					kmeans = KMeans(n_clusters=K).fit(points)
					lables = kmeans.predict(points)
					clusers = kmeans.cluster_centers_					
				except:
					print("error")
				print("key Thuat Toan")
			if 800 < mouse_x < 950 and 550 < mouse_y < 600 :
				K = 0
				Error = 0 
				points = []
				lables = []
				clusers = []
				print("key Reset")
	for i in range(len(points)):
		pygame.draw.circle(screen,black,(points[i][0]+52,points[i][1]+52),6)
		if lables == []:
			pygame.draw.circle(screen,white,(points[i][0]+52,points[i][1]+52),5)
		else:
			pygame.draw.circle(screen,color[lables[i]],(points[i][0]+52,points[i][1]+52),5)

	for i in range(len(clusers)):
		pygame.draw.circle(screen,color[i],(int(clusers[i][0])+52,int(clusers[i][1])+52),10)
		
	# draw calculate and draw error 
	Error = 0 
	if clusers != [] and lables != []:
		for i in range(len(points)):
			Error += distance(points[i],clusers[lables[i]])
	#draw error values 
	text_Error = font.render('Error = ' +str(int(Error)),True,black) 
	screen.blit(text_Error, (800,350))
	
	pygame.display.flip()
pygame.quit()	
