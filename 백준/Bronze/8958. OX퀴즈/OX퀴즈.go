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

	for i := 0; i<n; i++ {
		var s string
		fmt.Fscan(reader, &s)
		score := 0
		tmp := 0
		for _, v := range(s) {
			if v == 'O' {
				tmp += 1
			} else {
				tmp = 0
			}
			score += tmp
		}
		fmt.Fprintln(writer, score);		
	}
}