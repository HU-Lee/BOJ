package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	if n == 0 {
		fmt.Fprintln(writer, 0)
		return
	}

	arr := []int{}
	for i := 1; i<=n; i++ {
		var a int
		fmt.Fscanln(reader, &a)
		arr = append(arr, a)
	}

	sort.Ints(arr)

	cut := int(math.Round(float64(n) * 0.15))

	sum := 0;
	for _, val := range arr[cut: len(arr)-cut] {
		sum += val;
	}
	fmt.Fprintln(writer, int(math.Round(float64(sum) / float64(len(arr) - cut*2))))

}