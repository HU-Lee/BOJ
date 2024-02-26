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

	for i := 0; i<=4; i++ {
		r := n - 3*i
		if r < 0 {
			break
		}
		if r % 5 == 0 {
			fmt.Fprintln(writer, r/5+i)
			return
		}		
	}
	fmt.Fprintln(writer, -1)
}