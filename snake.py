import consts

class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def check_key(self, key):

        mov = self.keys[key]
        if mov == self.direction:
            return False
        elif mov == "LEFT" and self.direction == "RIGHT":
            return False
        elif mov == "RIGHT" and self.direction == "LEFT":
            return False
        elif mov == "UP" and self.direction == "DOWN":
            return False
        elif mov == "DOWN" and self.direction == "UP":
            return False
        else:
            return True

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):

        now_head = self.get_head()
        now_location_head = (self.val(now_head[0]+Snake.dx[self.direction]),
                             self.val(now_head[1]+Snake.dy[self.direction])
                             )
        # check kill
        if self.game.get_cell(now_location_head).color != consts.back_color and self.game.get_cell(now_location_head).color != consts.fruit_color:
            self.game.kill(self)
            return

        # add head_snake to list body cell
        self.cells.append(now_location_head)
        # complete food

        if self.game.get_cell(now_location_head).color != consts.fruit_color:
            pop_cell = self.cells.pop(0)
            self.game.get_cell(pop_cell).set_color(consts.back_color)
            self.game.get_cell(now_location_head).set_color(self.color)
        else:
            self.game.get_cell(now_location_head).set_color(self.color)

    def handle(self, keys):
        for key in keys:
            if key in self.keys:
                if self.check_key(key):
                    self.direction = self.keys[key]
                    break
