package com.funtap.awass;

import com.funtap.awass.Top10OWASPWeb2021.PayLoadSignature.A3Injection.SQLInjection;
import com.funtap.awass.postmainAPI.module;
import com.funtap.awass.postmainAPI.postmanJsonApi;
import com.funtap.awass.postmainAPI.sendRequest;
import net.minidev.json.parser.ParseException;

import java.io.IOException;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;

public class main {
    public static void main(String[] args) throws IOException, URISyntaxException, InterruptedException, ParseException {
        String json = "{\n" +
                "\t\"info\": {\n" +
                "\t\t\"_postman_id\": \"6df0e061-5a02-4742-8e97-cca7ef468a2f\",\n" +
                "\t\t\"name\": \"b\",\n" +
                "\t\t\"schema\": \"https://schema.getpostman.com/json/collection/v2.1.0/collection.json\"\n" +
                "\t},\n" +
                "\t\"item\": [\n" +
                "\t\t{\n" +
                "\t\t\t\"name\": \"login\",\n" +
                "\t\t\t\"request\": {\n" +
                "\t\t\t\t\"method\": \"POST\",\n" +
                "\t\t\t\t\"header\": [\n" +
                "\t\t\t\t\t{\n" +
                "\t\t\t\t\t\t\"key\": \"Host\",\n" +
                "\t\t\t\t\t\t\"value\": \"testphp.vulnweb.com\"\n" +
                "\t\t\t\t\t},\n" +
                "\t\t\t\t\t{\n" +
                "\t\t\t\t\t\t\"key\": \"Content-Length\",\n" +
                "\t\t\t\t\t\t\"value\": \"20\"\n" +
                "\t\t\t\t\t},\n" +
                "\t\t\t\t\t{\n" +
                "\t\t\t\t\t\t\"key\": \"Cache-Control\",\n" +
                "\t\t\t\t\t\t\"value\": \"max-age=0\"\n" +
                "\t\t\t\t\t},\n" +
                "\t\t\t\t\t{\n" +
                "\t\t\t\t\t\t\"key\": \"Upgrade-Insecure-Requests\",\n" +
                "\t\t\t\t\t\t\"value\": \"1\"\n" +
                "\t\t\t\t\t},\n" +
                "\t\t\t\t\t{\n" +
                "\t\t\t\t\t\t\"key\": \"Origin\",\n" +
                "\t\t\t\t\t\t\"value\": \"http://testphp.vulnweb.com\"\n" +
                "\t\t\t\t\t},\n" +
                "\t\t\t\t\t{\n" +
                "\t\t\t\t\t\t\"key\": \"Content-Type\",\n" +
                "\t\t\t\t\t\t\"value\": \"application/x-www-form-urlencoded\"\n" +
                "\t\t\t\t\t},\n" +
                "\t\t\t\t\t{\n" +
                "\t\t\t\t\t\t\"key\": \"User-Agent\",\n" +
                "\t\t\t\t\t\t\"value\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36\"\n" +
                "\t\t\t\t\t},\n" +
                "\t\t\t\t\t{\n" +
                "\t\t\t\t\t\t\"key\": \"Accept\",\n" +
                "\t\t\t\t\t\t\"value\": \"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\"\n" +
                "\t\t\t\t\t},\n" +
                "\t\t\t\t\t{\n" +
                "\t\t\t\t\t\t\"key\": \"Referer\",\n" +
                "\t\t\t\t\t\t\"value\": \"http://testphp.vulnweb.com/login.php\"\n" +
                "\t\t\t\t\t},\n" +
                "\t\t\t\t\t{\n" +
                "\t\t\t\t\t\t\"key\": \"Accept-Encoding\",\n" +
                "\t\t\t\t\t\t\"value\": \"gzip, deflate\"\n" +
                "\t\t\t\t\t},\n" +
                "\t\t\t\t\t{\n" +
                "\t\t\t\t\t\t\"key\": \"Accept-Language\",\n" +
                "\t\t\t\t\t\t\"value\": \"en-US,en;q=0.9\"\n" +
                "\t\t\t\t\t},\n" +
                "\t\t\t\t\t{\n" +
                "\t\t\t\t\t\t\"key\": \"Connection\",\n" +
                "\t\t\t\t\t\t\"value\": \"close\"\n" +
                "\t\t\t\t\t}\n" +
                "\t\t\t\t],\n" +
                "\t\t\t\t\"body\": {\n" +
                "\t\t\t\t\t\"mode\": \"raw\",\n" +
                "\t\t\t\t\t\"raw\": \"uname=test&pass=test\"\n" +
                "\t\t\t\t},\n" +
                "\t\t\t\t\"url\": {\n" +
                "\t\t\t\t\t\"raw\": \"http://testphp.vulnweb.com/userinfo.php\",\n" +
                "\t\t\t\t\t\"protocol\": \"http\",\n" +
                "\t\t\t\t\t\"host\": [\n" +
                "\t\t\t\t\t\t\"testphp\",\n" +
                "\t\t\t\t\t\t\"vulnweb\",\n" +
                "\t\t\t\t\t\t\"com\"\n" +
                "\t\t\t\t\t],\n" +
                "\t\t\t\t\t\"path\": [\n" +
                "\t\t\t\t\t\t\"userinfo.php\"\n" +
                "\t\t\t\t\t]\n" +
                "\t\t\t\t}\n" +
                "\t\t\t},\n" +
                "\t\t\t\"response\": []\n" +
                "\t\t}\n" +
                "\t]\n" +
                "}";
        postmanJsonApi p = new postmanJsonApi();
        List<module> Listob = new ArrayList<>();
        Listob  = p.readJson(json);
        SQLInjection sql = new SQLInjection();
        String[] payload = sql.getArrPaySQLin();
        String[] sig = sql.getArrSigSQLin();
        for (module u : Listob ){
            System.out.println(u.toString());
            sendRequest req = new sendRequest();
            req.requets(u,payload,sig);
        }

    }
}