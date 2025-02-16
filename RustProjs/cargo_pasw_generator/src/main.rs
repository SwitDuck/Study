use rand::Rng;  
use std::io;  

fn generate_password(length: usize) -> String {  //создается функция длиной usize и должна вернуть строку
    let chars = "0123456789"; //задается симвроы которые могут быть перебираться
    
    let mut rng = rand::thread_rng(); //создание изменяемой перементтой rng с рандомной генерацией значения
    let password: String = (0..length) //должно быть тут происходит генерация пароля размером от 0 до заданной длины, но я не понял как работает
        .map(|_| {
            let idx = rng.gen_range(0..chars.len());
            chars.chars().nth(idx).unwrap()
        })
        .collect();

    password
}

fn main() { //главная функция с инициализацией других функций в коде
    println!("Введите длину пароля:");
    
    let mut input = String::new(); //ввод для переменной из функции выше Length.Что такое new() не понял
    io::stdin().read_line(&mut input).expect("Ошибка ввода");
    
    let length: usize = input.trim().parse().expect("Введите число!");
    
    let password = generate_password(length);
    println!("Сгенерированный пароль: {}", password);
}
