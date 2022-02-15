package com.funtap.awass;

import com.funtap.awass.Entity.UrlOb;
import com.funtap.awass.Exploit.joomla_exploit;
import com.funtap.awass.SpiderWeb.SpiderWeb;
import com.funtap.awass.Top10OWASPWeb2021.Scan.A3Injection.SQLinjection;
import okhttp3.*;
import org.springframework.boot.SpringApplication;

import java.io.IOException;
import java.net.URISyntaxException;
import java.util.List;
public class main {
    public static void main(String[] args) throws IOException, URISyntaxException, InterruptedException {
        joomla_exploit joomla= new joomla_exploit();

        System.out.println(joomla.com_jce("https://www.bahiasanagustin.es/",null));
        }

}
