package main

import (
	"bufio"
	"fmt"
	"os"
)

func contains(s []int, e int) bool {
    for _, a := range s {
        if a == e {
            return true
        }
    }
    return false
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var arr []int

	for i := 0; i < 10; i++ {
		var n int
		fmt.Fscanln(reader, &n)
		r := n % 42
		if !contains(arr, r) {
			arr = append(arr, r)
		}
	}

	fmt.Fprintln(writer, len(arr))
}

// go run template.go
