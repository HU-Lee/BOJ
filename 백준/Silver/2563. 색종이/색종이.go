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

	var arr [100][100]int

	for i := 0; i < n; i++ {
		var a,b int
		fmt.Fscanln(reader, &a, &b)

		for m := a; m < a+10; m++ {
			for n := b; n < b+10; n++ {
				arr[m][n] = 1
			}
		}
	}
	all := 0
	for i := 0; i < 100; i++ {
		for j := 0; j < 100; j++ {
			all += arr[i][j]
		}
	}
	fmt.Fprintln(writer, all)
}