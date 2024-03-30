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

	dic1 := make(map[int]int)
	dic2 := make(map[int]int)

	for i := 0; i < 3; i++ {
		var x,y int
		fmt.Fscanln(reader, &x, &y)

		dic1[x]++
		dic2[y]++
	}
	m1, m2 := 0, 0
	for key, value := range dic1 {
		if value == 1 {
			m1 = key
		}
	}
	for key, value := range dic2 {
		if value == 1 {
			m2 = key
		}
	}
	fmt.Fprintln(writer, m1, m2)
}
