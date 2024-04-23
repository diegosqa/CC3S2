package org.example;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class MoneyTest {

    @Test
    public void testMoneyConstructor() {
        // Crea una instancia de Money con 100 USD y verifica si los valores son correctos.
        Money money = new Money(100, "USD");
        assertNotNull(money); // Verifica que el objeto creado no sea nulo.
        assertEquals(100, money.getAmount()); // Verifica que el monto es el esperado.
        assertEquals("USD", money.getCurrency()); // Verifica que la moneda es la esperada.
    }

    @Test
    public void testMoneyEqualitySameCurrencyAndAmount() {
        // Prueba que dos instancias de Money con los mismos valores son consideradas iguales.
        Money moneyOne = new Money(100, "USD");
        Money moneyTwo = new Money(100, "USD");
        assertEquals(moneyOne, moneyTwo);
    }

    @Test
    public void testMoneyEqualityDifferentAmount() {
        // Verifica que dos instancias de Money con la misma moneda pero diferentes cantidades no sean iguales.
        Money moneyOne = new Money(100, "USD");
        Money moneyTwo = new Money(50, "USD");
        assertNotEquals(moneyOne, moneyTwo);
    }

    @Test
    public void testMoneyEqualityDifferentCurrency() {
        // Verifica que dos instancias de Money con la misma cantidad pero diferentes monedas no sean iguales.
        Money moneyOne = new Money(100, "USD");
        Money moneyTwo = new Money(100, "EUR");
        assertNotEquals(moneyOne, moneyTwo);
    }

    @Test
    public void testMoneyEqualityNull() {
        // Verifica que una instancia de Money no es igual a `null`.
        Money money = new Money(100, "USD");
        assertNotEquals(money, null);
    }

    @Test
    public void testMoneyEqualityDifferentType() {
        // Verifica que una instancia de Money no es igual a un objeto de un tipo diferente.
        Money money = new Money(100, "USD");
        String notMoney = "Not a Money Object";
        assertNotEquals(money, notMoney);
    }
}

