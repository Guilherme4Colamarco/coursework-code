package com.mycompany.atividades_praticas_1.heranca;
public class Gerente extends Funcionario { public Gerente(double salarioBase){ super(salarioBase); } public double pagamentoComoGerente(){ return salarioBase*1.20; } }
