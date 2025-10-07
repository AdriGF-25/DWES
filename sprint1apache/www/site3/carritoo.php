<?php
$carrito = [
    "Manzana" => 0.60,   // Precio actualizado
    "Pan" => 1.30,       // Precio actualizado
    "Leche" => 0.90,     // Nuevo producto
    "Queso" => 2.50,     // Nuevo producto
    "Huevos" => 1.80     // Nuevo producto
];

$total = 0;
?>

<table>
    <tr>
        <th>Producto</th>
        <th>Precio</th>
    </tr>

    <?php foreach ($carrito as $producto => $precio): ?>
        <tr>
            <td><?php echo $producto; ?></td>
            <td><?php echo $precio; ?>€</td>
        </tr>
        <?php $total += $precio; ?>
    <?php endforeach; ?>

    <tr>
        <td>TOTAL:</td>
        <td><?php echo $total; ?>€</td>
    </tr>
</table>