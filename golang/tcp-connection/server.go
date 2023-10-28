package main

import (
	"fmt"
	"io"
	"net"
)

func main() {
	ln, err := net.Listen("tcp", "localhost:10000")
	if err != nil {
		panic(err)
	}
	fmt.Println("Server running at localhost:10000")
	waitClient(ln)
}

func waitClient(ln net.Listener) {
	conn, err := ln.Accept()
	if err != nil {
		panic(err)
	}
	go goEcho(conn)
	waitClient(ln)
}

func goEcho(conn net.Conn) {
	defer conn.Close()
	echo(conn)
}

func echo(conn net.Conn) {

	var buf = make([]byte, 1024)

	n, err := conn.Read(buf)
	if err != nil {
		if err == io.EOF {
			return
		}
		panic(err)
	}
	fmt.Printf("Client> %s \n", buf)

	n, err = conn.Write(buf[:n])
	if err != nil {
		panic(err)
	}
	echo(conn)
}
