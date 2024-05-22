package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var arr []int = []int{}
var ans int = 0

func contains(arr []int, val int) bool {
	for _, v := range arr {
		if v == val {
			return true
		}
	}
	return false
}

func dfs(x int, n int) {
	if x == n {
		ans++
		return
	} else {
		for i := 0; i < n; i++ {
			isSafe := true
			for j := 0; j < x; j++ {
				if contains(arr, i) || int(math.Abs(float64(i-arr[j]))) == x-j {
					isSafe = false
					break
				}
			}
			if isSafe {
				arr = append(arr, i)
				dfs(x+1, n)
				arr = arr[:len(arr)-1]
			}
		}
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	dfs(0, n)

	fmt.Fprintln(writer, ans)
}
