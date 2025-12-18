n = North
s = South
e = East
w = West

def move_to_origin():
	while get_pos_x() > 0:
		if get_pos_x() > get_world_size() / 2:
			move(e)
		else:
			move(w)
	while get_pos_y() > 0:
		if get_pos_y() > get_world_size() / 2:
			move(n)
		else:
			move(s)

move_to_origin()
