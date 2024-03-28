package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)


func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	for {
		var a,b,c int
		fmt.Fscanln(reader, &a, &b, &c)

		arr := []int{a,b,c}
		sort.Ints(arr)

		if arr[2] == 0 {
			break
		}

		if arr[0]+arr[1] <= arr[2] {
			fmt.Fprintln(writer, "Invalid")
		} else if arr[0] == arr[2] {
			fmt.Fprintln(writer, "Equilateral")
		} else if arr[0] == arr[1] || arr[1] == arr[2] {
			fmt.Fprintln(writer, "Isosceles")
		} else {
			fmt.Fprintln(writer, "Scalene")
		}
	}
}

// go run template.go
