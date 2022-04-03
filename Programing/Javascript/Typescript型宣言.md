---
tags:
  - Typescript
  - 覚書
---

# Typescript による型定義

## 基本的な型の定義

### 定義できる型の一覧

| string               | 文字列型               | 備考           |
| -------------------- | ---------------------- | -------------- |
| number               | 数値型                 |                |
| boolean              | 真偽値型               |                |
| undefined            | 未定義の値の型         |                |
| function             | 関数型                 |                |
| object               | オブジェクト型         |                |
| any                  | 何でも型               | Typescript独自 |
| { a: number }        | オブジェクトリテラル型 | Typescript独自 |
| (a: number)=> number | 関数型                 | Typescript独自 |

### 型の定義

```typescript
// 単一変数の型定義
let name: string

name = 'Mike'  // Success.
name = 1       // Error!

// オブジェクトリテラルの型定義
const person: { name: string, age: number} = {
  name: '太郎',
  age: 20,
}

// 関数の引数と戻り値の定義
function call_log(message: string): number {
  console.log(message)
  return 0
}

call_log('Hello!')
```

## 自分で作成した型の定義

```typescript
type Person = { name: string, age: number }

const person: Person = {
  name: 'Taro',
  age: 22,
}
```
