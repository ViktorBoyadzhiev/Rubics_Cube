# class RubiksCube:
#     def __init__(self):
#         self.state = {
#             'U': [['U1', 'U2', 'U3'], ['U4', 'U5', 'U6'], ['U7', 'U8', 'U9']],
#             'F': [['F1', 'F2', 'F3'], ['F4', 'F5', 'F6'], ['F7', 'F8', 'F9']],
#             'R': [['R1', 'R2', 'R3'], ['R4', 'R5', 'R6'], ['R7', 'R8', 'R9']],
#             'L': [['L1', 'L2', 'L3'], ['L4', 'L5', 'L6'], ['L7', 'L8', 'L9']],
#             'B': [['B1', 'B2', 'B3'], ['B4', 'B5', 'B6'], ['B7', 'B8', 'B9']],
#             'D': [['D1', 'D2', 'D3'], ['D4', 'D5', 'D6'], ['D7', 'D8', 'D9']]
#         }
#
#     def rotate_face_clockwise(self, face):
#         # Rotate the specified face clockwise
#         self.state[face] = [list(reversed(col)) for col in zip(*self.state[face])]
#
#     def rotate_face_counter_clockwise(self, face):
#         # Rotate the specified face counter-clockwise
#         self.state[face] = [list(col) for col in reversed(list(zip(*self.state[face])))]
#
#     def __str__(self):
#         # Convert the cube's state to a string for printing
#         return '\n'.join([' '.join(row) for face in ['U', 'F', 'R', 'L', 'B', 'D'] for row in self.state[face]])
#
#
# # Example usage:
# cube = RubiksCube()
# print("Initial state:")
# print(cube)
#
# cube.rotate_face_clockwise('U')
# print("\nAfter rotating the top face clockwise:")
# print(cube)
#
# cube.rotate_face_counter_clockwise('F')
# print("\nAfter rotating the front face counter-clockwise:")
# print(cube)


# 1. Check matrix-wise the rotation of the cube and the correct implementation
# 1.1 Implement shuffling of the cube on start
# 2. See TKinter lib to create a visual representation (maybe)
# 3. Make more game-like - have a DB with 5 best times - implement a timer


import numpy as np


class RubiksCube:

    SIDES = {
        'U': ['F', 'L', 'B', 'R'],
        'F': ['U', 'R', 'D', 'L'],
        'R': ['F', 'U', 'B', 'D'],
        'L': ['U', 'F', 'D', 'B'],
        'B': ['U', 'L', 'D', 'R'],
        'D': ['F', 'R', 'B', 'L'],
    }

    def __init__(self):
        # Initialize the Rubik's Cube with each face as a 3x3 array
        self.state = {
            'U': np.array([['U1', 'U2', 'U3'], ['U4', 'U5', 'U6'], ['U7', 'U8', 'U9']]),
            'F': np.array([['F1', 'F2', 'F3'], ['F4', 'F5', 'F6'], ['F7', 'F8', 'F9']]),
            'R': np.array([['R1', 'R2', 'R3'], ['R4', 'R5', 'R6'], ['R7', 'R8', 'R9']]),
            'L': np.array([['L1', 'L2', 'L3'], ['L4', 'L5', 'L6'], ['L7', 'L8', 'L9']]),
            'B': np.array([['B1', 'B2', 'B3'], ['B4', 'B5', 'B6'], ['B7', 'B8', 'B9']]),
            'D': np.array([['D1', 'D2', 'D3'], ['D4', 'D5', 'D6'], ['D7', 'D8', 'D9']])
        }

    def rotate_face_clockwise(self, face):
        # Rotate the specified face clockwise
        self.state[face] = np.rot90(self.state[face], k=-1)
        TODO: "add rotation in the sides according to the face the direction"

    def rotate_face_counter_clockwise(self, face):
        # Rotate the specified face counter-clockwise
        self.state[face] = np.rot90(self.state[face])
        TODO: "add rotation in the sides according to the face the direction"

    def __str__(self):
        # To display the cube
        return '\n'.join([' '.join(row) for face in ['U', 'F', 'R', 'L', 'B', 'D'] for row in self.state[face]])


# Example usage:
cube = RubiksCube()
print("Initial state:")
print(cube)

cube.rotate_face_clockwise('U')
print("\nAfter rotating the top face clockwise:")
print(cube)

cube.rotate_face_counter_clockwise('F')
print("\nAfter rotating the front face counter-clockwise:")
print(cube)
