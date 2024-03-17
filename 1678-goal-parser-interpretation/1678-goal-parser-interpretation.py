class Solution:
    def interpret(self, command: str) -> str:
        hashmap = {'()': 'o', '(al)': 'al'}

        for key, value in hashmap.items():
            command = command.replace(key, value)
        return command