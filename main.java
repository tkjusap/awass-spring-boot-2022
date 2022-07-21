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
        postmanJsonApi p = new postmanJsonApi();
        List<module> Listob = new ArrayList<>();
        Listob  = p.readJson();
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
