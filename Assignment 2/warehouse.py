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
        self.matrix = [[-1, -1, -1, -1, -1, -1], [-1, 0, 1, -1, -1, -1], [-1, 0, 0, -1, -1, -1], [-1, 3, 0, 0, 0, -1], [-1, 0, 0, 2, 0, -1], [-1, 0, 0, -1, -1, -1], [-1, -1, -1, -1, -1, -1]]
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
        if action == 'UP':
            if self.matrix[self.agent_position[0], self.agent_position[1] - 1] == -1:
                reward = -1

            elif self.matrix[self.agent_position[0], self.agent_position[1] - 1] == 2 and self.matrix[self.agent_position[0], self.agent_position[1] - 2] == -1:
                reward = -1

            elif self.matrix[self.agent_position[0], self.agent_position[1] - 1] == 2:

                self.matrix[self.agent_position[0], self.agent_position[1] - 1] = 1
                self.matrix[self.agent_position[0], self.agent_position[1]] = 0
                self.matrix[self.agent_position[0], self.agent_position[1] - 2] = 2

                self.box_location[1] = self.box_location[1] - 1
                self.agent_position[1] = self.agent_position[1] - 1

            else:
                self.matrix[self.agent_position[0], self.agent_position[1] - 1] = 1
                self.matrix[self.agent_position[0], self.agent_position[1]] = 0
                self.agent_position[1] = self.agent_position[1] - 1

        elif action == 'DOWN':
            
            print(self.agent_position[0])
            if self.matrix[self.agent_position[0]][self.agent_position[1] + 1] == -1:
                reward = -1

            elif self.matrix[self.agent_position[0], self.agent_position[1] + 1] == 2 and self.matrix[self.agent_position[0], self.agent_position[1] + 2] == -1:
                reward = -1

            elif self.matrix[self.agent_position[0], self.agent_position[1] + 1] == 2:

                self.matrix[self.agent_position[0], self.agent_position[1] + 1] = 1
                self.matrix[self.agent_position[0], self.agent_position[1]] = 0
                self.matrix[self.agent_position[0], self.agent_position[1] + 2] = 2

                self.box_location[1] = self.box_location[1] + 1
                self.agent_position[1] = self.agent_position[1] + 1

            else:
                self.matrix[self.agent_position[0], self.agent_position[1] + 1] = 1
                self.matrix[self.agent_position[0], self.agent_position[1]] = 0
                self.agent_position[1] = self.agent_position[1] + 1

        elif action == 'LEFT':
            
            if self.matrix[self.agent_position[0] - 1][self.agent_position[1]] == -1:
                reward = -1

            elif self.matrix[self.agent_position[0] - 1, self.agent_position[1]] == 2 and self.matrix[self.agent_position[0] - 2, self.agent_position[1]] == -1:
                reward = -1

            elif self.matrix[self.agent_position[0] - 1, self.agent_position[1]] == 2:

                self.matrix[self.agent_position[0] - 1, self.agent_position[1]] = 1
                self.matrix[self.agent_position[0], self.agent_position[1]] = 0
                self.matrix[self.agent_position[0] - 2, self.agent_position[1]] = 2

                self.box_location[0] = self.box_location[0] - 1
                self.agent_position[0] = self.agent_position[0] - 1

            else:
                self.matrix[self.agent_position[0] - 1, self.agent_position[1]] = 1
                self.matrix[self.agent_position[0], self.agent_position[1]] = 0
                self.agent_position[0] = self.agent_position[0] - 1

        else:
            
            if self.matrix[self.agent_position[0] + 1, self.agent_position[1]] == -1:
                reward = -1

            elif self.matrix[self.agent_position[0] + 1, self.agent_position[1]] == 2 and self.matrix[self.agent_position[0] + 2, self.agent_position[1]] == -1:
                reward = -1

            elif self.matrix[self.agent_position[0] + 1, self.agent_position[1]] == 2:

                self.matrix[self.agent_position[0] + 1, self.agent_position[1]] = 1
                self.matrix[self.agent_position[0], self.agent_position[1]] = 0
                self.matrix[self.agent_position[0] + 2, self.agent_position[1]] = 2

                self.box_location[0] = self.box_location[0] + 1
                self.agent_position[0] = self.agent_position[0] + 1

            else:
                self.matrix[self.agent_position[0] + 1, self.agent_position[1]] = 1
                self.matrix[self.agent_position[0], self.agent_position[1]] = 0
                self.agent_position[0] = self.agent_position[0] + 1


        if self.box_location == self.goal_location:
            reward = 1
            done = True
        elif self.box_location not in self.valid_states:
            done = True
            reward = -1
            print(self.agent_position)

        else:
            reward = -1

        return self.agent_position, reward, done
    
    def render(self):
        """Function to get the simulation of the warehouse agent system 
        """
        print(self.matrix)

env = WarehouseAgent()

env.render()

first = env.step('DOWN')
print(first)
env.render()
