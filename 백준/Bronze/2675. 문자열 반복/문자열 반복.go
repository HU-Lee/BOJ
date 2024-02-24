package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	for i := 0; i < n; i++ {
		var a int
		var b string
		fmt.Fscanln(reader, &a, &b)
		for _, s := range b {
			fmt.Fprint(writer, strings.Repeat(string(s), a))
		}
		fmt.Fprintln(writer);
	}
}
