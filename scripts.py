# Entities
e_b = Entities.Bush
e_c = Entities.Carrot
e_g = Entities.Grass
e_p = Entities.Pumpkin

# Directions
n = North
s = South
e = East
w = West

# Items
water = num_items(Items.Water)
ground_water_level = get_water()

# functions for harvesting
def h_e(entity, direction=None):
	if ground_water_level < 0.5 and water <= 64:
		use_item(Items.Water)
		
	if can_harvest():
		harvest()
		plant(entity)
		if(direction):
			move(direction)
	else:
		if(direction):
			if(entity == e_p):
				plant(entity)
				move(direction)
			else:
				move(direction)
		if(direction == None):
			plant(entity)
def h():
	if can_harvest():
		harvest()
		
def is_even(n):
	if n % 2 == 0:
		return True
		
def sp_h(rows, columns, entity):
	r = rows
	c = columns
	cr = 0
	
	while cr < r:
		if is_even(cr):
			for i in range(c - 1):
				h_e(entity, e)
			h_e(entity)
			move(n)
			cr = cr + 1
		else:
			for i in range(c - 1):
				h_e(entity, w)
			h_e(entity)
			move(n)
			cr = cr + 1
			
while True:
	sp_h(8, 8, e_c)
