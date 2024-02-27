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

	var arr []int
	for i := 0; i < n; i++ {
		var i int
		fmt.Fscanln(reader, &i)
		if i > 0 {
			arr = append(arr, i)
		} else {
			l := len(arr)
			arr = append(arr[:l-1], arr[l:]...)
		}
	}
	sum := 0
	for _, i := range arr {
		sum += i
	}
	fmt.Fprintln(writer, sum)
}