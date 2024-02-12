const express = require('express');
const bodyParser = require('body-parser');
const fetch = require('node-fetch');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/submit/', (req, res) => {
    // Отправка данных в телеграмм

    const telegramToken = '6921274787:AAGYV8h4UwjzwcNyhA6nXYCRyrCQnC2Z97g';
    const chatId = '1332500391';

    const formData = req.body;

    // Ваш код для формирования сообщения в телеграмм
    const message = `
        Заказ торта по фото:

        Контактное лицо: ${formData.contactPerson}
        Номер телефона: ${formData.phoneNumber}
        Email: ${formData.email}
        Дата выполнения заказа: ${formData.deliveryDate}
        Город: ${formData.city}
        Эскиз: ${formData.sketch ? 'Прикреплен' : 'Не прикреплен'}
        Выбранная начинка: ${formData.filling}
        Количество килограмм: ${formData.weight}
        Примечание: ${formData.note || 'Отсутствует'}
    `;

    // Отправка сообщения в телеграмм
    fetch(`https://api.telegram.org/bot${telegramToken}/sendMessage`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            chat_id: chatId,
            text: message,
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Message sent to Telegram:', data);
        res.send('Заказ отправлен успешно!');
    })
    .catch(error => {
        console.error('Error sending message to Telegram:', error);
        res.status(500).send('Произошла ошибка при отправке заказа.');
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
