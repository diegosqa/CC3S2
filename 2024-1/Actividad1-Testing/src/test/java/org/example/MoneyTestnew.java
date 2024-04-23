package org.example;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;
import org.junit.jupiter.params.provider.Arguments;

import java.util.stream.Stream;

public class MoneyTestnew {

    @ParameterizedTest
    @MethodSource("provideMoneyForConstructorTest")
    public void testMoneyConstructor(int amount, String currency) {
        // Utiliza datos parametrizados para verificar la creación correcta de instancias de Money.
        Money money = new Money(amount, currency);
        assertNotNull(money); // Verifica que el objeto creado no sea nulo.
        assertEquals(amount, money.getAmount()); // Verifica que el monto es el esperado.
        assertEquals(currency, money.getCurrency()); // Verifica que la moneda es la esperada.
    }

    private static Stream<Arguments> provideMoneyForConstructorTest() {
        // Provee un stream de argumentos para la prueba parametrizada del constructor.
        return Stream.of(
            Arguments.of(100, "USD"),
            Arguments.of(200, "EUR"),
            Arguments.of(0, "JPY"),
            Arguments.of(-1, "USD") // Incluso se prueba con un monto negativo.
        );
    }

    @ParameterizedTest
    @MethodSource("provideMoneyForEqualityTest")
    public void testMoneyEquality(Money moneyOne, Money moneyTwo, boolean expected) {
        // Utiliza datos parametrizados para verificar varias condiciones de igualdad entre instancias de Money.
        assertEquals(expected, moneyOne.equals(moneyTwo));
    }

    private static Stream<Arguments> provideMoneyForEqualityTest() {
        // Provee un stream de argumentos para la prueba parametrizada de igualdad.
        Money money100USD = new Money(100, "USD");
        Money money200USD = new Money(200, "USD");
        Money money100EUR = new Money(100, "EUR");
        Money money100USD2 = new Money(100, "USD");

        return Stream.of(
            Arguments.of(money100USD, money100USD2, true), // misma moneda y cantidad
            Arguments.of(money100USD, money200USD, false), // misma moneda, cantidad diferente
            Arguments.of(money100USD, money100EUR, false), // moneda diferente, misma cantidad
            Arguments.of(money100USD, null, false), // comparación con null
            Arguments.of(money100USD, "Not a Money Object", false) // comparación con un tipo diferente
        );
    }
}


