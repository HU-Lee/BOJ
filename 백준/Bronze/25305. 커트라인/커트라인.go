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

	var n,k int 
	fmt.Fscanln(reader, &n, &k)

	arr := make([]int, n)
	for i := 0; i < n; i++ {
		var x int
		fmt.Fscan(reader, &x)
		arr[i] = x
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if arr[i] < arr[j] {
				arr[i], arr[j] = arr[j], arr[i]
			}
		}
	}
	fmt.Fprintln(writer, arr[k-1])
}

// go run template.go
