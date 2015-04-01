package com.company;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.BlockingQueue;

/**
 * Created by grzegorz on 01.04.15.
 */
public class Producer implements Runnable {

    protected BlockingQueue queue = null;


    public Producer(BlockingQueue queue) {
        this.queue = queue;
    }

    public void run() {

        ServerSocket listener = null;
        try {
            listener = new ServerSocket(9090);
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            while (true) {
                Socket socket = listener.accept();
                try {


                    BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                    String answer = input.readLine();
                    System.out.println(answer);
                } finally {
                    socket.close();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            assert listener != null;
            try {
                listener.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }



        //pipe version working
        /*
        while(true) {
            Runtime rt = Runtime.getRuntime();
            String[] commands = {"cat", "pipe"};
            Process proc = null;
            try {
                proc = rt.exec(commands);
            } catch (IOException e) {
                e.printStackTrace();
            }

            BufferedReader stdInput = new BufferedReader(new InputStreamReader(proc.getInputStream()));

            String s = null;
            try {
                while(s == null) {
                    s = stdInput.readLine();
                }

                queue.add(s);

                } catch (IOException e) {
                e.printStackTrace();
            }
        }
        */

        }


    }




