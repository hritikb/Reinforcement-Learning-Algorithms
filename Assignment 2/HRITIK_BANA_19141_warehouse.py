"""
Definition of the Warehouse Agent environment
"""

class WarehouseAgent():
    def __init__(self):
        """
        Initializing the environment
        """
        self.GRID_DIM = [6,7]

        self.agent_position = [1,2]

        self.box_location = [4,3]
        self.goal_location = [3,1]

        # self.matrix will keep track of the current board situation. In this representation, walls and forbidden regions
        # are denoted by '-1', empty squares are denoted by '0', agent is denoted by '1', box is denoted by '2', and goal
        # location is denoted by '3'
        self.matrix = [[-1, -1, -1, -1, -1, -1], [-1, 0, 1, -1, -1, -1], [-1, 0, 0, -1, -1, -1], [-1, 3, 0, 0, 0, -1], [-1, 0, 0, 2, 0, -1], [-1, 0, 0, -1, -1, -1], [-1, -1, -1, -1, -1, -1]]
        
        # if the agent pushes the box next to the wall (other than the left wall along which the goal location also lies
        # then no matter what action, the agent cannot bring the box away from the wall and hence will never be able to take 
        # the box to the goal location. self.valid_states contains all the states which will not lead to such situations.
        self.valid_states = [[2, 1], [2, 2], [3, 1], [3, 2], [3, 3], [4, 1], [4, 2], [4, 3]]

    def reset(self):
        """Function to reset the environment at the end of each episode to its initial state configuration

        Returns:
            state: the state of the environment reset to its initial conditions
        """
        self.agent_position = [1,2]

        self.box_location = [4,3]

        self.matrix = [[-1, -1, -1, -1, -1, -1], [-1, 0, 1, -1, -1, -1], [-1, 0, 0, -1, -1, -1], [-1, 3, 0, 0, 0, -1], [-1, 0, 0, 2, 0, -1], [-1, 0, 0, -1, -1, -1], [-1, -1, -1, -1, -1, -1]]

        # we will return a tuple containing the coordinates of the agent and box respectively
        return self.agent_position,  self.box_location
    
    def step(self, action):
        """Function to control and evaluate the agents' action

        Args:
            action: pass on the action which the agent needs to take at that time step
            action_space: ['UP', 'DOWN', 'LEFT', 'RIGHT']

        Returns:
            new_state: the new state agent reaches after taking the action
            reward: the reward obtained on taking the action
            done: boolean value to determine if episode terminating condition is reached
        """
        done = False
        if action == 'LEFT':

            # if wall is on the left
            if self.matrix[self.agent_position[0]][self.agent_position[1] - 1] == -1: 
                reward = -1

            # if box is on the left, but to the left of box is the wall.
            elif self.matrix[self.agent_position[0]][self.agent_position[1] - 1] == 2 and self.matrix[self.agent_position[0]][self.agent_position[1] - 2] == -1:
                reward = -1

            # when the box is on the left, and the wall is not to the left of box.
            elif self.matrix[self.agent_position[0]][self.agent_position[1] - 1] == 2:

                self.matrix[self.agent_position[0]][self.agent_position[1] - 1] = 1
                self.matrix[self.agent_position[0]][self.agent_position[1]] = 0
                self.matrix[self.agent_position[0]][self.agent_position[1] - 2] = 2

                self.box_location[1] = self.box_location[1] - 1
                self.agent_position[1] = self.agent_position[1] - 1

            # when neither the wall nor the box is to the left of the agent.    
            else:
                self.matrix[self.agent_position[0]][self.agent_position[1] - 1] = 1
                self.matrix[self.agent_position[0]][self.agent_position[1]] = 0
                self.agent_position[1] = self.agent_position[1] - 1

        elif action == 'RIGHT':
            
            # if wall is on the right
            if self.matrix[self.agent_position[0]][self.agent_position[1] + 1] == -1:
                reward = -1

            # if box is on the right, but to the right of box is the wall.
            elif self.matrix[self.agent_position[0]][self.agent_position[1] + 1] == 2 and self.matrix[self.agent_position[0]][self.agent_position[1] + 2] == -1:
                reward = -1

            # when the box is on the right, and the wall is not to the right of box.
            elif self.matrix[self.agent_position[0]][self.agent_position[1] + 1] == 2:

                self.matrix[self.agent_position[0]][self.agent_position[1] + 1] = 1
                self.matrix[self.agent_position[0]][self.agent_position[1]] = 0
                self.matrix[self.agent_position[0]][self.agent_position[1] + 2] = 2

                self.box_location[1] = self.box_location[1] + 1
                self.agent_position[1] = self.agent_position[1] + 1

            # when neither the wall nor the box is to the right of the agent.    
            else:
                self.matrix[self.agent_position[0]][self.agent_position[1] + 1] = 1
                self.matrix[self.agent_position[0]][self.agent_position[1]] = 0
                self.agent_position[1] = self.agent_position[1] + 1

        elif action == 'UP':
            
            # if wall is above
            if self.matrix[self.agent_position[0] - 1][self.agent_position[1]] == -1:
                reward = -1

            # if box is above, but above the box is the wall.
            elif self.matrix[self.agent_position[0] - 1][self.agent_position[1]] == 2 and self.matrix[self.agent_position[0] - 2][self.agent_position[1]] == -1:
                reward = -1

            # when the box is above, and the wall is not above the box.
            elif self.matrix[self.agent_position[0] - 1][self.agent_position[1]] == 2:

                self.matrix[self.agent_position[0] - 1][self.agent_position[1]] = 1
                self.matrix[self.agent_position[0]][self.agent_position[1]] = 0
                self.matrix[self.agent_position[0] - 2][self.agent_position[1]] = 2

                self.box_location[0] = self.box_location[0] - 1
                self.agent_position[0] = self.agent_position[0] - 1

            # when neither the wall nor the box is above the agent.    
            else:
                self.matrix[self.agent_position[0] - 1][self.agent_position[1]] = 1
                self.matrix[self.agent_position[0]][self.agent_position[1]] = 0
                self.agent_position[0] = self.agent_position[0] - 1

        elif action == 'DOWN':
            
            # if wall is below
            if self.matrix[self.agent_position[0] + 1][self.agent_position[1]] == -1:
                reward = -1

            # if box is below, but below the box is the wall.
            elif self.matrix[self.agent_position[0] + 1][self.agent_position[1]] == 2 and self.matrix[self.agent_position[0] + 2][self.agent_position[1]] == -1:
                reward = -1

            # when the box is below, and the wall is not below the box.
            elif self.matrix[self.agent_position[0] + 1][self.agent_position[1]] == 2:

                self.matrix[self.agent_position[0] + 1][self.agent_position[1]] = 1
                self.matrix[self.agent_position[0]][self.agent_position[1]] = 0
                self.matrix[self.agent_position[0] + 2][self.agent_position[1]] = 2

                self.box_location[0] = self.box_location[0] + 1
                self.agent_position[0] = self.agent_position[0] + 1

            # when neither the wall nor the box is below the agent.    
            else:
                self.matrix[self.agent_position[0] + 1][self.agent_position[1]] = 1
                self.matrix[self.agent_position[0]][self.agent_position[1]] = 0
                self.agent_position[0] = self.agent_position[0] + 1


        if self.box_location == self.goal_location:
            reward = 0
            done = True
        elif self.box_location not in self.valid_states:
            done = True
            reward = -1

        else:
            reward = -1

        return self.agent_position, reward, done
    
    def render(self):
        """Function to get the simulation of the warehouse agent system 
        """
        print(*self.matrix, sep = '\n')

# Commands to check if the environment is working fine
env = WarehouseAgent()

env.render()
first = env.step('DOWN')
sec = env.step('DOWN')
th = env.step('RIGHT')
fou = env.step('RIGHT')
fif = env.step('DOWN')
six = env.step('LEFT')
sev = env.step('LEFT')
eig = env.step('DOWN')
nin = env.step('LEFT')
ten = env.step('UP')
print(ten)
env.render()