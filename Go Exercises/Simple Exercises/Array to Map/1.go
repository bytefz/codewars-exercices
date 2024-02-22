// Write a Go program that converts an existing array into a map.

package main

import (
	"fmt"
	"strconv"
)

// An array cannot be a parameter, just slices
func arr2map(arr []int ) map[string]int{
	tempMap := make(map[string]int,len(arr))

	for index, value := range arr{
		index := strconv.Itoa(index)
		tempMap[index] = value
	}

	return tempMap
}

func main() {
	arr := [6]int{1,2,3,4,5,6}
	// Create slice out of the array.
	arrS := arr[:]
	newMap := arr2map(arrS)
	fmt.Println(newMap)
}