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

	var a,b,c int
	fmt.Fscanln(reader, &a, &b, &c)

	arr := []int{a,b,c}
	sort.Ints(arr)

	if arr[0]+arr[1] > arr[2] {
		fmt.Fprintln(writer, arr[0]+arr[1]+arr[2])
	} else {
		fmt.Fprintln(writer, 2*arr[0]+2*arr[1]-1)
	}
}

// go run template.go
