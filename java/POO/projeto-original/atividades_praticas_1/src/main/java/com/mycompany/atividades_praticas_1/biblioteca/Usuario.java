package com.mycompany.atividades_praticas_1.biblioteca;
public class Usuario { protected String nome; protected String endereco; public Usuario(String nome,String endereco){ this.nome=nome; this.endereco=endereco; } public String getTipo(){ return "Usuário"; } public void exibirDados(){ System.out.println(getTipo()+": "+nome+" - "+endereco); } }
