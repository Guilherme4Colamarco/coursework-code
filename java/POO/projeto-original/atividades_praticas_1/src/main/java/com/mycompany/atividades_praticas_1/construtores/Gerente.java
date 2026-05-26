package com.mycompany.atividades_praticas_1.construtores;
public class Gerente extends Funcionario { private String departamento; public Gerente(String nome,double salario,String departamento){ super(nome,salario); this.departamento=departamento; } public void mostrarInfo(){ System.out.println("Gerente: "+nome+", salário R$ "+salario+", departamento "+departamento); } }
