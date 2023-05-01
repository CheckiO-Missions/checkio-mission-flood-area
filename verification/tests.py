"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""
from collections.abc import Iterable
from collections import defaultdict
from random import randint
BS, SL = '\\', '/'


def flood_area(diagram: str) -> Iterable[int]:
    flood = defaultdict(int)
    stack = []
    for cur, terrain in enumerate(diagram):
        if terrain == BS:
            stack.append(cur)
        elif terrain == SL and stack:
            first = stack.pop()
            for (f_first, f_last) in list(flood):
                if first < f_first < cur:
                    flood[(first, cur)] += flood.pop((f_first, f_last))
            flood[(first, cur)] += cur - first
    return flood

randoms = []
for i in (10, 20, 40, 60, 80):
    terrain = ''.join(r'/\_'[randint(0, 2)] for _ in range(i))
    answer = flood_area(terrain)
    randoms.append({
            'input': [terrain],
            "answer": list(answer.values()),
            "explanation": list(answer.keys()),})

TESTS = {
    "Randoms": randoms,
    "Basics": [
        {
            "input": [r'\\//'],
            "answer": [4],
            "explanation": [[0, 3]],
        },
        {
            "input": [r'_/\//'],
            "answer": [1],
            "explanation": [[2, 3]],
        },
        {
            "input": [r'\\/_'],
            "answer": [1],
            "explanation": [[1, 2]],
        },
        {
            "input": [r'\\_\\_/_/\//_'],
            "answer": [18],
            "explanation": [[1, 11]],
        },
        {
            "input": [r'////\\_\///__' + '\\'],
            "answer": [11],
            "explanation": [[4, 10]],
        },
        {
            "input": [r'/\\\\_\\\/\\_/\\\_\/\/\//_/\/_///\/////'],
            "answer": [220],
            "explanation": [[2, 38]],
        },
        {
            "input": [r'\____\____\/\/\\____/_\/_____/_/___/\_'],
            "answer": [84],
            "explanation": [[0, 35]],
        },
    ],
    'Edges': [
        # 11
        {
            "input": [r'_'],
            "answer": [],
            "explanation": [[]],
        },
        # 12
        {
            "input": [r'\\'],
            "answer": [],
            "explanation": [[]],
        },
        # 13
        {
            "input": [r'/'],
            "answer": [],
            "explanation": [[]],
        },
        # 14
        {
            "input": [r'/'+'\\'],
            "answer": [],
            "explanation": [[]],
        },
        # 15
        {
            "input": [r'\_'],
            "answer": [],
            "explanation": [[]],
        },
        # 16
        {
            "input": [r'_/'],
            "answer": [],
            "explanation": [[]],
        },
        # 17
        {
            "input": [r'_\/_'],
            "answer": [1],
            "explanation": [[1, 2]],
        },
        # 18
        {
            "input": [r'_/\_'],
            "answer": [],
            "explanation": [[]],
        },
    ],
    'Extra': [
        # 19
        {
            "input": [r'\\///\_/\/\\\\/_/\\///_\\\\\/_/'+'\\'],
            "answer": [4, 2, 1, 19, 5],
            "explanation": [[0, 3], [11, 21], [5, 7], [8, 9], [26, 30]],
        },
        # 20
        {
            "input": [r'\/\\\_/\\//__\/_/\/\__/'],
            "answer": [1, 20, 1, 3],
            "explanation": [[0, 1], [3, 16], [17, 18], [19, 22]],
        },
        # 21
        {
            "input": [r'\\\\//\/\_/\\\\/_/\\///_'+'\\\\\\'],
            "answer": [4, 1, 2, 19],
            "explanation": [[12, 22], [2, 5], [6, 7], [8, 10]],
        },
        # 22
        {
            "input": [r'\//\//\\\/\\\/\\///\\//__\\\\/\//\\/'],
            "answer": [1, 1, 1, 12, 4, 7, 1],
            "explanation": [[0, 1], [8, 9], [3, 4], [27, 32], [11, 18], [19, 22], [34, 35]],
        },
        # 23
        {
            "input": [r'////\/\\\/\\\\/\\\\\_/_/\//\/\\\_'],
            "answer": [1, 1, 1, 17, 1],
            "explanation": [[8, 9], [4, 5], [13, 14], [17, 26], [27, 28]],
        },
        # 24
        {
            "input": [r'_//\///_/\////\_///\/\\/\\\_\/'+'\\'],
            "answer": [1, 1, 2, 1, 1, 1],
            "explanation": [[3, 4], [9, 10], [28, 29], [14, 16], [22, 23], [19, 20]],
        },
        # 25
        {
            "input": [r'/\//\\\\\\\_/\\//////'],
            "answer": [1, 50],
            "explanation": [[1, 2], [6, 20]],
        },
        # 26
        {
            "input": [r'\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/'+'\\'],
            "answer": [4, 2, 1, 19, 9],
            "explanation": [[0, 3], [11, 21], [5, 7], [8, 9], [28, 35]],
        },
        # 27
        {
            "input": [r'\/\\\\___/\\\\\/\\//\_/\\\\\//\_//\/\\\\//\//__\/\\\\/'],
            "answer": [1, 4, 1, 4, 2, 14, 1, 12, 1, 1],
            "explanation": [[0, 1], [5, 9], [14, 15], [16, 19], [20, 22], [37, 44], [47, 48], [25, 33], [34, 35], [52, 53]],
        },
        # 28
        {
            "input": [r'\////\_////\///\//\\\\\/\\\\\\/\\///_/\///\/////\\\_/\\\/'],
            "answer": [1, 2, 1, 1, 153, 2, 1],
            "explanation": [[0, 1], [5, 7], [55, 56], [11, 12], [50, 52], [15, 16], [19, 47]],
        },
        # 29
        {
            "input": [r'_\/_\__\___\__/_/__\///\__/\\\__/_\\\___/\\/__/_\\\___/'],
            "answer": [1, 30, 3, 3, 4, 6, 4],
            "explanation": [[1, 2], [4, 21], [29, 32], [23, 26], [36, 40], [41, 46], [50, 54]],
        },
        # 30
        {
            "input": [r'_\__\\/\_/\_\_\_\\__'],
            "answer": [1, 2],
            "explanation": [[5, 6], [7, 9]],
        },
        # 31
        {
            "input": [r'/___//\\\/\_/\\___/_\\\\/\\//\_\\/\\\_\/\/__/_/_/_'],
            "answer": [1, 2, 4, 1, 4, 1, 35],
            "explanation": [[8, 9], [10, 12], [14, 18], [23, 24], [25, 28], [32, 33], [34, 48]],
        },
        # 32
        {
            "input": [r'_\\_\/__\\__\\/___/__\//\///__\/__/\__/\\_//\\\\\\\/\_\\__/_/_/\_\//\_\\/_/\\\__\_///\_\___/////\\\_'],
            "answer": [101, 3, 6, 147],
            "explanation": [[49, 95], [1, 34], [35, 38], [39, 43]],
        },
        # 33
        {
            "input": [r'\/\\__\__\/\///_/_/\_\____/\_\_/_///\\/\_\/__/\\/\_//__\\\//\_\_\\/\\_/\______/\\\/_\\/\/\/_/\///\\/\_\/_//\_/_///\\_\\//_\\\\_/_/__\_//_/\\_\//\/__\__/\__//\\\/\\/\//\\/_/_\_\_\\_\///_\____\_\\__/'+'\\\\\\'],
            "answer": [1, 34, 28, 1, 7, 9, 4, 216, 4, 36, 30, 1, 7, 5, 11, 3],
            "explanation": [[0, 1], [2, 16], [56, 59], [117, 120], [122, 137], [138, 156], [62, 113], [19, 34], [37, 38], [39, 45], [46, 52], [177, 183], [159, 160], [161, 166], [167, 171], [193, 196]],
        },
        # 34
        {
            "input": [r'\\\\\_\/\_\\\\/\__\_/_/\__/\\_\\\//_/__\_/_\\\\\\///_\/_\\///\____\_\/\\//____\\\_\_\\\\\\/\\///\\\\/\\\/\\//\___/_///\_\\\__\\\__\/\\////\/__/_\\\__\\\\_/\\/\\\\_/\\/_\\\/\_\\\/\\\\\/\_\/\___\\\//\_/'],
            "answer": [1, 1, 9, 3, 10, 2, 29, 1, 4, 12, 57, 43, 2, 1, 2, 1, 1, 1, 1, 1, 4, 2],
            "explanation": [[6, 7], [13, 14], [15, 22], [23, 26], [45, 60], [30, 36], [39, 41], [68, 69], [70, 73], [98, 117], [88, 95], [125, 142], [152, 154], [156, 157], [161, 163], [165, 166], [170, 171], [176, 177], [182, 183], [186, 187], [193, 196], [197, 199]],
        },
        # 35
        {
            "input": [r'\/\_/\/__////////_/\/_\__\\\/__/_/////\/\\_\\_\\//////_/\_//\\//___/___\_\\/_//////\_/\/\/_/\//\_///\/_/_/\\/_/\/_/\//__\//____///\_/_///_///\//_\_\//////_/\//\/\//_//_/\_\/\_\\/\/////\/\_/_/___/__\_/'],
            "answer": [1, 2, 1, 1, 26, 1, 42, 2, 4, 12, 2, 1, 1, 1, 2, 1, 5, 1, 1, 1, 2, 1, 5, 1, 1, 1, 29, 1, 2, 2],
            "explanation": [(0, 1), (2, 4), (5, 6), (19, 20), (22, 34), (38, 39), (40, 53), (56, 58), (60, 63), (71, 78), (83, 85), (86, 87), (88, 89), (92, 93), (95, 97), (100, 101), (106, 110), (111, 112), (115, 116), (120, 121), (130, 132), (141, 142), (145, 149), (156, 157), (159, 160), (161, 162), (169, 182), (184, 185), (186, 188), (197, 199)],
        },
        # 36
        {
            "input": [r'_//\/_/\__\______\_____/__/\________/_\/____/////__/__/_//\/\___/___\/_/\__\_\_\__/___/_//\_\_/____/\\/\\//__/___\\/_//__/_\__\__/\___\\_///\____/_\______\_///\__//___/\_\//_/\\\__\____/_\_/__/___\/_'+'\\'],
            "answer": [1, 69, 1, 4, 1, 42, 11, 14, 5, 70, 3, 5, 22, 1],
            "explanation": [(3, 4), (7, 44), (58, 59), (60, 64), (68, 69), (72, 89), (90, 99), (100, 109), (113, 117), (123, 158), (159, 162), (177, 192), (196, 197), (168, 172)],
        },
        # 37
        {
            "input": [r'//_\_\\\\\\\/_\_//\\/\\\\\__\_\////\\_\\\/\_\\\\\\\/\\\/\\\/__\\\\/\//\\\\\\\\_\\\\\_\\__\_/\\\\\\__\\\//\/\_\\\\_//\\\\\/_\__\__\\\\\\\_\_\_\\\/\\///\\\\_\\\/\\\\\\\\\_/\/\\\_\\_\\\\/\\\/\\\\\\\\\\//_\_\__\\\/__\\\\\__\\\\\\\/\\\\\\\_\\\\\_/\\////\\\/_\\\/_/\_\\_/\/\/__\\\\/_\\\\_\\\\\\\\\//_\\\_\_\\\\\/\\\\\\_/_\/\/\//\\\\//_/\/\\//\\\\\/\\//\_\/\\\\\/\____/_/\\\_\//\\\\\\\_\\\\\_'+'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'],
            "answer": [10, 1, 23, 1, 1, 1, 1, 7, 2, 4, 1, 6, 1, 12, 1, 2, 1, 1, 1, 4, 1, 1, 24, 1, 5, 2, 1, 1, 1, 4, 1, 16, 10, 1, 4, 1, 4, 1, 16, 5],
            "explanation": [(19, 20), (10, 17), (24, 34), (40, 41), (50, 51), (54, 55), (58, 59), (64, 69), (89, 91), (101, 104), (105, 106), (111, 115), (120, 121), (142, 149), (157, 158), (167, 169), (170, 171), (182, 183), (186, 187), (196, 199), (208, 209), (225, 226), (250, 251), (254, 258), (237, 247), (262, 264), (265, 266), (267, 268), (274, 275), (289, 292), (304, 305), (323, 329), (330, 331), (332, 335), (310, 321), (340, 341), (342, 345), (348, 349), (353, 363), (366, 370)],
        },
        # 38
        {
            "input": [r'_//\__////___/\/\/_///_/\/\/_//\__///\///\\////___/\\_\/////_///\\///\///_///\\///_////\_/\/\\/\///_///////_///\/_///_///\/_/////\_/////_/////\/\//\_///\_/////__\//_//\/_//\//_/\/\/////__////\__/_/\_//_/\_/\\_/////\__//\/\//_///\/__////_\/\//\/////_//\/_/\/__////\_///_\//////\/_//_//_/_//_///////\///_//////___/\//////_\/\////////__\/_/\_///////\//\/////_/\\\//_/\\/___\/\//\//\_\\\_////_\\\/\\/\_/_'],
            "answer": [3, 1, 1, 1, 1, 3, 1, 4, 11, 4, 1, 4, 2, 1, 7, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 3, 2, 2, 6, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 10, 13, 1, 21, 1, 1, 2],
            "explanation": [(3, 6), (14, 15), (16, 17), (24, 25), (26, 27), (31, 34), (37, 38), (41, 44), (51, 57), (64, 67), (69, 70), (77, 80), (87, 89), (90, 91), (92, 97), (111, 112), (121, 122), (129, 131), (142, 143), (144, 145), (147, 149), (152, 154), (161, 162), (167, 168), (172, 173), (177, 178), (179, 180), (191, 194), (197, 199), (203, 205), (206, 210), (214, 217), (219, 220), (221, 222), (228, 229), (237, 238), (239, 240), (242, 243), (251, 252), (255, 256), (263, 265), (269, 270), (276, 277), (297, 298), (312, 313), (320, 321), (322, 323), (333, 334), (337, 339), (346, 347), (349, 350), (394, 395), (396, 398), (391, 392), (357, 363), (364, 374), (375, 376), (378, 387)],
        },
        # 39
        {
            "input": [r'\///\\//\//\/\/\\/\\/\//\\///\/\\\\\\\\////\\\/\\\\\///////\\\/\///\//\\/\/\//\\///\\\//\\//\///\//\\////\//\\\/\//////\\/\//\\\\////\///////\\\\/\\\/\//\///\/\/\/\/\/\///\\\///\/\//\\\\//\/\\//\\//\\\/\///\\//\//////\////\/\\//\/\//\\\\/\\\\/\\//\////\/\\/\\/////\/\/\\\\//\\////\/\\\\//\/\////\\/\/////\///\\/\/\\\/\\//\/\\\\//\\//\///\\\/////\//\/\/\/////\/\\////\\\/\\\/\\/\\\\//\\/\\///\\\/\/\///\\//\/\/\/\/\\\/\\\\\/\\/\\\//\/\\//\\\\/\///\\\\\\/\////\\\\\//\/\\\\/\\\\//\\\/\///////\/\\\\\\\/'],
            "answer": [1, 4, 1, 1, 1, 25, 1, 334, 4, 1, 14, 7, 16, 1, 93, 9, 1, 1, 92, 1, 1, 4, 1, 1, 227, 7, 1, 150, 1, 1, 1, 1, 4, 1, 1, 1, 4, 12, 19, 4, 1, 1, 1, 1, 1, 1, 1, 4, 1, 4, 14, 23, 4, 1, 87, 1, 1],
            "explanation": [(0, 1), (4, 7), (8, 9), (11, 12), (13, 14), (15, 28), (29, 30), (31, 98), (99, 102), (105, 106), (108, 115), (498, 499), (119, 124), (125, 132), (133, 134), (468, 489), (490, 491), (461, 464), (465, 466), (141, 170), (171, 176), (177, 178), (179, 180), (182, 213), (448, 457), (438, 445), (217, 218), (427, 430), (431, 432), (433, 436), (424, 425), (421, 422), (222, 223), (224, 227), (228, 229), (230, 231), (233, 294), (295, 300), (415, 416), (304, 305), (379, 382), (383, 390), (391, 400), (401, 404), (405, 406), (407, 408), (409, 410), (411, 412), (308, 347), (348, 349), (350, 351), (352, 353), (375, 376), (372, 373), (358, 359), (360, 363), (368, 369)],
        },
        # 40
        {
            "input": [r'\//\\\\\\\//\\///\/\\\\\\\\//\/\\/\\/\\\\\\/\\\\/\\/\\/\\\\\\\\/\/\\///\\\\//\/\\\\\\\\/\/\\\\//\//\/\//\\\\\/\\\\\\/\/\\\\\/\\\//\/\/\\//\\/\\\\\\\\\/\\\\\\\\\\///\\\/\\///\\/\\/\/\\\\/\/\\\\\\\\\/\//\\\\\\\/\\/\\\/\/\\/\\\\//\\\/\\\\/\\\\\\\\/\/\//\/\\\\/\\/\\\\//\\/\\\\\/\\\\\\\\\\/\/\\\//\/\/\//\\\\\/\//\/\/\\\/\\\\/\/\///\\///\\//\\\\///\\/\/\\\/\\\\\/\//\//\\\\\\\\///\\\\\\//\/\///\/\\\\\//\\\//\/////\\/\/\//\\\\\\//\\/\\\\\\\\/\/\//\\\\\\\\//\\\\\/\\\\\\\\\\\\/\\\\\/\\\\//\/\//\/\\\/\/\/'+'\\'],
            "answer": [1, 17, 1, 4, 1, 1, 1, 1, 1, 1, 1, 15, 4, 1, 1, 1, 27, 1, 1, 1, 1, 4, 1, 1, 4, 1, 1, 9, 12, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1, 4, 1, 1, 10, 1, 1, 1, 4, 1, 1, 1, 1, 18, 7, 1, 1, 1, 38, 4, 9, 1, 1, 1, 17, 9, 26, 1, 61, 10, 4, 1, 10, 4, 1, 1, 1, 15, 1, 1, 1, 1],
            "explanation": [(0, 1), (7, 16), (17, 18), (32, 33), (25, 28), (29, 30), (35, 36), (42, 43), (47, 48), (50, 51), (53, 54), (73, 76), (77, 78), (61, 70), (86, 87), (88, 89), (90, 103), (108, 109), (115, 116), (117, 118), (123, 124), (139, 140), (126, 129), (130, 131), (132, 133), (134, 137), (149, 150), (174, 175), (165, 172), (158, 163), (177, 178), (179, 180), (184, 185), (186, 187), (195, 200), (207, 208), (210, 211), (214, 215), (216, 217), (219, 220), (223, 226), (229, 230), (234, 235), (242, 249), (250, 251), (255, 256), (258, 259), (267, 268), (262, 265), (273, 274), (284, 285), (286, 287), (288, 299), (303, 308), (309, 310), (311, 312), (315, 316), (317, 332), (333, 336), (345, 346), (347, 348), (338, 343), (351, 352), (355, 364), (378, 389), (390, 391), (392, 409), (410, 417), (370, 375), (422, 425), (427, 428), (435, 442), (449, 452), (457, 458), (470, 471), (476, 477), (493, 494), (495, 496), (497, 498), (479, 488), (489, 490)],
        },
    ],
}
