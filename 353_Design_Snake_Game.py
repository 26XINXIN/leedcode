from collections import deque

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = food
        self.n_food = 0
        self.snake = deque([[0, 0]])
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        # print(self.snake)
        
        x, y = self.snake[0]
        if direction == 'U':
            xx, yy = x, y - 1
        elif direction == 'D':
            xx, yy = x, y + 1
        elif direction == 'L':
            xx, yy = x - 1, y
        elif direction == 'R':
            xx, yy = x + 1, y
        # print(direction, (xx, yy))
        
        # collide with border
        if xx < 0 or xx >= self.width or yy < 0 or yy >= self.height:
            return - 1
        
        # collide with itself
        for i in range(len(self.snake) - 1):
            if self.snake[i][0] == xx and self.snake[i][1] == yy:
                return - 1
        
        # eats food
        if self.n_food < len(self.food) and yy == self.food[self.n_food][0] and xx == self.food[self.n_food][1]:
            self.snake.appendleft([xx, yy])
            self.n_food += 1
            return len(self.snake) - 1
        
        self.snake.appendleft([xx, yy])
        self.snake.pop()
        return len(self.snake) - 1
            


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)