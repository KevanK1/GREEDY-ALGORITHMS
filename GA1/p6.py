def maximum_units(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    total_units = 0

    for numberOfBoxes, numberOfUnitsPerBox in boxTypes:
        if truckSize <= 0:
            break
        boxes_to_take = min(truckSize, numberOfBoxes)
        total_units += boxes_to_take * numberOfUnitsPerBox
        truckSize -= boxes_to_take

    return total_units

boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4

print(maximum_units(boxTypes, truckSize))  # Output: 8