package main

import (
	"bufio"
	"fmt"
	"os"
)


func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	n := 5

	arr := make([]int, n)
	sum := 0
	for i := 0; i < n; i++ {
		var x int
		fmt.Fscanln(reader, &x)
		arr[i] = x
		sum += x
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if arr[i] > arr[j] {
				arr[i], arr[j] = arr[j], arr[i]
			}
		}
	}
	fmt.Fprintln(writer, sum/5)
	fmt.Fprintln(writer, arr[n/2])
}

// go run template.go
