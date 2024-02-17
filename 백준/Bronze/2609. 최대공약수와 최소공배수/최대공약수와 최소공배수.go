package main

import (
	"bufio"
	"fmt"
	"os"
)

func gcd(a int, b int) int {
	if a%b == 0 {
		return b
	} else {
		return gcd(b, a%b)
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	
	defer writer.Flush()

	var a,b int
	fmt.Fscanf(reader, "%d %d",&a, &b)

	if a >= b {
		fmt.Fprintln(writer, gcd(a,b))
		fmt.Fprintln(writer, a*b/gcd(a,b))
	} else {
		fmt.Fprintln(writer, gcd(b,a))
		fmt.Fprintln(writer, a*b/gcd(a,b))
	}
}