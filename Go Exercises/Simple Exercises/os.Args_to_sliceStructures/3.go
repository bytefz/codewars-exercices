/*
Write a Go utility that converts os.Args into
a slice of structures with fields for storing the index and the value
of each command-line argument—you should define the structure
that is going to be used on your own.
*/

package main

import (
	"fmt"
	"os"
)

type Console struct{
	Index int
	Value string
}

func main(){
	var sliceConsole []Console

	args := os.Args

	if len(args) < 2 {
		fmt.Println("Have to insert data on command-line!!!")
		return 
	}

	data := args[1:]

	for index, value := range data{
		console := Console{Index: index, Value: value}
		sliceConsole = append(sliceConsole, console)
	}

	fmt.Println("Slice of Console:", sliceConsole)
}