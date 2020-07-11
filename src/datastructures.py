
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "first_name": "John Jackson",
                "age": 33,
                "lucky_numbers": [7, 13, 22],
                "id":1
            },
            {
                "first_name": "Jane Jackson",
                "age": 35,
                "lucky_numbers": [10, 14, 3],
                "id":2
            },
            {
                "first_name": "Jimmy Jackson",
                "age": 5,
                "lucky_numbers": [7],
                "id":3
            }

        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return len(self._members)+1  #randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        print('==>datastructures.add_member:', member)

        if ('id' not in member.keys()):
            id = self._generateId()
            print('id=',id)  
            member['id'] = id
        
        self._members.append(member)
        return member

    def delete_member(self, id):
        # fill this method and update the return
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)
                return None
        

    def get_member(self, id):
        # fill this method and update the return
        print('datastructures.get_member.id=',id)
        for m in self._members:
            if m["id"] == int(id):
                return m

        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members