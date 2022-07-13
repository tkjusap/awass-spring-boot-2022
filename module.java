package com.funtap.awass.postmainAPI;

import java.util.List;

public class module {
    private String Url;
    private String Method;
    private List<header> header;
    private String body;

    public module() {
    }

    public module(String url, String method, List<header> header, String body) {
        Url = url;
        Method = method;
        this.header = header;
        this.body = body;
    }

    public String getUrl() {
        return Url;
    }

    public void setUrl(String url) {
        Url = url;
    }

    public String getMethod() {
        return Method;
    }

    public void setMethod(String method) {
        Method = method;
    }

    public List<header> getHeader() {
        return header;
    }

    public void setHeader(List<header> header) {
        this.header = header;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
}
class header{
    private String key;
    private String value;

    public header() {
    }

    public header(String key, String value) {
        this.key = key;
        this.value = value;
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
}