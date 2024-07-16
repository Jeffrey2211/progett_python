blocks = int(input("Enter the number of blocks: "))

height = 0
used_blocks = 0

# Loop to determine the height of the pyramid
while used_blocks + (height + 1) <= blocks:
    height += 1        # Increase the height by 1
    used_blocks += height  # Add the current height to the used blocks

print("The height of the pyramid:", height)

