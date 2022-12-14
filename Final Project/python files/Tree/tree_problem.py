'''
Practice Problem using the Tree Data Structure
'''

'''
This tree will represent a platoon in the United States Army.
A platoon is a group of soldiers anywhere from 18-50 men, in 
this case it has 40 men. A platoon is 
organized into squads, and squads into teams. In this example,
each squad will have 10 men and each team will have 5 men, 
being 4 squads and 8 teams total. The platoon is led by a Lieutenant, each
squad is led by a Staff Sergeant, and each Team is led by a 
Team Leader. These three ranks, along with Private (basic soldier)
are the four basic ranks in a platoon. 

Most of the code has been done for you, you only need to learn
how it works and then fix the errors.
'''

class Platoon:
    class Soldier:
        def __init__(self, data):
            self.name = data["name"]
            self.rank = data["rank"]
            self.left = None
            self.right = None
            
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Platoon.Soldier(data)
        if self.root is None:
            self.root = node
        else:
            self._insert(data, self.root)

    def _insert(self, new_node, node):
        if node is None:
            return
        elif node.left is None:
            node.left = new_node
            return
        elif node.right is None:
            node.right = new_node
            return
        height_left = self.get_height(node.left)
        height_right = self.get_height(node.right)
        if height_left < height_right:
            self._insert(new_node, node.left)
        else: 
            self._insert(new_node, node.right)
    
    def get_height(self, node):
        if node is None:
            return 0
        else:
            return self._get_height(node)

    def _get_height(self, node):
        if node == None:
            return 0
        else:
            count_left = 1 + self._get_height(node.left)
            count_right = 1 + self._get_height(node.right)

        return count_left if count_left >= count_right else count_right

    def __str__(self):
        if self.root is None:
            return ''
        else:
            self._str(self.root)
            return ''

    def _str(self, node):
        if node != None:
            print(f"Name: {node.name}, \tRank: {node.rank}")
            self._str(node.left)
            self._str(node.right)

# Make the soldiers' data structures
platoon = Platoon()
squads = 4          # number of squads in a platoon
teams = 2           # number of teams in a squad
soldiers = 5        # number of soldiers in a team
names = ''
with open("python files/Tree/male_names.txt") as f:
    names = f.read().splitlines()
for squad in range(squads):
    for team in range(teams):
        for soldier in range(soldiers):
            soldier_num = squad * teams * soldiers + team * soldiers + soldier
            name = names[soldier_num]
            if soldier_num == 0:
                rank = "Lieutenant"
            elif 0 < soldier_num <= 4:
                rank = "Staff Sergeant"
            elif 4 < soldier_num <= 12:
                rank = "Team Leader"
            else:
                rank = "Private"
            soldier_info = {
                "name": name,
                "rank": rank,
            }
            platoon.insert(soldier_info)
print(platoon);