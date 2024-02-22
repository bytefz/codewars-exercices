// Write a Go program that converts an existing map into
// two slices—the first slice contains the keys of the map whereas
// the second slice contains the values.
// The values at index n of the two slices should correspond to a key and value pair
// that can be found in the original map.

package main

import (
	"fmt"
)


func main(){
	examMap := map[string]string{
		"nombre": "Franzua",
		"apellido": "Plasencia",
		"edad": "22",
	}
	sliceKey := make([]string, 0)
	sliceValue := make([]string, 0)
	
	for key, value := range examMap {
		sliceKey = append(sliceKey, key)
		sliceValue = append(sliceValue, value)
	}
	fmt.Printf("Slice de Llaves: %v\nSlice de Valores: %v\n", sliceKey, sliceValue)
}