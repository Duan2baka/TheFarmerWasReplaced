clear()
def init_drone():
	while True:
		move(North)
		move(East)
		print("hi")

spawn_drone(init_drone)
while True:
	do_a_flip()
	move(East)