# strings in python are immutable

selfish = "This is a cool sentence"
# 01234567

print(selfish[0])

# [start:stop]

print(selfish[0:3])

# [start:stop:stepover]

print(selfish[0:7:2])

print(selfish[1:])

print(selfish[-7])

# Reverse an order
print(selfish[::-1])

print(len(selfish))

# String methods
yell_chill = selfish.upper()
print(yell_chill)

whisper_chill = selfish.lower()
print(whisper_chill)
