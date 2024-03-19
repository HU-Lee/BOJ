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

	var n int
	fmt.Fscanln(reader, &n)

	arr := make([]int, n)
	for i := 0; i < n; i++ {
		var x int
		fmt.Fscanln(reader, &x)
		arr[i] = x
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if arr[i] > arr[j] {
				arr[i], arr[j] = arr[j], arr[i]
			}
		}
	}
	for i := 0; i < n; i++ {
		fmt.Fprintln(writer, arr[i])
	}
}

// go run template.go
