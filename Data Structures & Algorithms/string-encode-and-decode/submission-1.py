class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedMessage = list()
        for message in strs:
            l = list(ord(character) for character in message)
            lStr = list(str(number) for number in l)
            encoded = "-".join(lStr)
            encodedMessage.append(encoded)
        return str(len(strs)) + ";" + ";".join(encodedMessage)

    def decode(self, s: str) -> List[str]:
        countStr, rest = s.split(";", 1)
        count = int(countStr)
        if count == 0:
            return []

        decodedMessages = list()
        l = rest.split(";")
        for encoded in l:
            if len(encoded) == 0:
                decodedMessages.append(encoded)
            else:
                currentDecoded = encoded.split("-")
                numbers = list(int(number) for number in currentDecoded)
                lNumbers = list(chr(number) for number in numbers)
                decodedMessages.append("".join(lNumbers))
        return decodedMessages