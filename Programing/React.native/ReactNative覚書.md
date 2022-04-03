---
tags:
  - ReactNative
  - Expo
  - 覚書
---

# React Native (+ Expo) 覚書

## 1. コンポーネント関連

### 1.1. コンポーネントの設定と呼び出し

```javascript
// Main
export default function App() {
  return (
    <View style={styles.container}>
      <Welcome name="Naoki" />
    </View>
  );
}

// Component
function Welcome(props) {
  return <Text>Hello, {props.name}</Text>
}
```

### 1.2. 別ファイルからのコンポーネント呼び出し

```javascript
import { Welcome } from './js/conponents';

// Main
export default function App() {
  return (
    <View style={styles.container}>
      <Welcome fname="Amanda" />
    </View>
  );
}

// Code in ./js/conponents.js
import React from 'react';
import { Text } from 'react-native';

export function Welcome(props) {
  return <Text>Hello, {props.fname}</Text>
}
```

## 2. 状態管理関連

### 2.1. useState による状態管理

- `useState`は『変数名』『変数を操作する関数名』で使用する。
- `useState`で作成された値が変化すると、自動的に再描画される。

```javascript
import React, { useState } from 'react'
import { View, Text, Button } from 'react-native'

export default function App() {
  const [cntNum, setNum] = useState(0)

  return (
    <View>
      <Button title="+1" onPress={() => setNum(cntNum + 1)} />
      <Text>{cntNum}</Text>
      <Button title="-1" onPress={() => setNum(cntNum - 1)} />
      <Button title="Reset!" onPress={() => setNum(0)} />
    </View>
  )
}
```

`useState`は関数コンポーネントの最初に、必ず呼び出さなければならない。
従って、当該関数外で値を変化させる事はできない。

複雑な条件式に基づく値の変化を`return`の外にまとめたい場合は、
`const`で同じ関数内にまとめる必要がある。

```javascript
import React, { useState } from 'react'
import { View, Text, Button } from 'react-native'

export default function App() {
  const [cntNum, setNum] = useState(5)

  const count_down = () => {
    if (cntNum > 0)
    setNum(cntNum - 1)
  }

  return (
    <View>
    <Text>{cntNum}</Text>
    <Button title='Count Down' onPress={count_down}/>
    </View>
  )
}
```

### 2.2. useEffect による状態管理

- `useEffect`はコンポーネントが読み込まれた（マウント）際、自動で実行される。
- `return`でコンポーネントが削除（アンマウント）された際の挙動を指定する。
- `useEffect`自身には再描画のトリガーとなる機能は存在しないが、
以下のような方法で再描画させる事が可能
  - 処理内に`setInterval`などで`useState`を含ませる。
  - 画面遷移のタイミングで`AsyncStorage.getItem`を実行、`setData`等を行う。

```javascript
// useEffect は関数内に記述する。
import React, { useState, useEffect } from 'react'
import { View, Text } from 'react-native'

export default function App() {
  const [nowDate, setDate] = useState(() => new Date())

  useEffect(() => {
    const timerID = setInterval(() => {
      setDate(new Date())
    }, 1000)

    return () => {
      clearInterval(timerID)
    }
  }, [])

  return (
    <View>
      <Text>{nowDate.toLocaleTimeString()}</Text>
    </View>
  )
}
```

```javascript
// useEffect を分離する場合
import React, { useState, useEffect } from 'react'
import { View, Text } from 'react-native'

export default function App() {
  const date = Clock()
  return (
    <View>
      <Text>{date.toLocaleTimeString()}</Text>
    </View>
  )
}

function Clock() {
  const [nowDate, setDate] = useState(() => new Date())

  useEffect(() => {
    const timerID = setInterval(() => {
      setDate(new Date())
    }, 1000)

    return () => {
      clearInterval(timerID)
    }
  }, [])

  return nowDate
}
```

### 2.3. 画面遷移のタイミングで useEffect の実行

```javascript
useEffect(() => {
  const initialize = async () => {
    const listData = await loadAll()
    setList(listData)
  }
  // focus を指定すると、画面が開かれた際に第二引数の内容を実行する。
  // これにより navigation.goBack などで画面が遷移先から戻ってきた場合も initialize 関数を実行している。
  const unsubscribe = navigation.addListener('focus', initialize)
  return unsubscribe
}, [navigation])
```

### 2.4. useLayoutEffect

`useEffect`とほぼ同じ動作をするが、実行タイミングが異なる。

このため、画面描画時にちらつきが発生する場合は、`useLayoutEffect`が有効となる。

特に`switch`コンポーネントなどに効果大

- `useEffect`
  - ステータスを変更して、再レンダリングする
  - Reactはレンダリングを開始する
  - 画面に描画する
  - **`useEffect`を実行**
- `useLayoutEffect`
  - ステータスを変更して、再レンダリングする
  - Reactはレンダリングを開始する
  - **`useLayoutEffect`を実行**
  - 画面に描画する

## 3. スタイル指定関連

### 3.1. 基本的なスタイル指定

```javascript
import { Text, StyleSheet } from 'react-native'

export default function App() {
  return(
    <Text style={{fontSize: 10}}>直接指定</Text>
    <Text style={styles.blackFont}>変数指定</Text>
    <Text style={[styles.balckFont, styles.bigFont]}>複数指定</Text>
  )
}

const styles=SytleSheet.create({
  blackFont: {
    color: 'black',
  },
  bigFont: {
    fontSize: 24,
  },
})
```

### 3.2. View の装飾

大きさの指定に関するもの

```text
width  : 横幅（数値指定、パーセント指定）
height : 縦幅（           〃           ）

minWidth : 横幅の最小値（数値指定、パーセント指定）
maxWidth : 横幅の最大値（           〃           ）
minHeight: 縦幅の最小値（           〃           ）
maxHeight: 縦幅の最大値（           〃           ）
```

内・外の配置に関するもの

```text
margin  : View の外側に設ける余白の幅

marginTop    : 上側の余白幅（数値指定、パーセント指定）
marginBottom : 下側の余白幅（           〃           ）
marginLeft   : 左側の余白幅（           〃           ）
marginRight  : 右側の余白幅（           〃           ）

padding : View の内側に設ける余白の幅（数値指定、パーセント指定）

paddingTop    : 上側の余白幅（数値指定、パーセント指定）
paddingBottom : 下側の余白幅（           〃           ）
paddingLeft   : 左側の余白幅（           〃           ）
paddingRight  : 右側の余白幅（           〃           ）
```

アイテムの並べ方に関する物

```text
flex: 個々のアイテムを均等に割り付けるかどうか（1: 有効）

flexDirection : アイテムの並べ方（column: 縦方向  row: 横方向）
flexWrap      : アイテムの折り返し（wrap, nowrap, wrap-reverse）
```

枠線の太さに関するもの

```text
borderWidth       : 枠線の太さ

borderTopWitdh    : 枠線の太さ（上）
borderBottomWidth : 枠線の太さ（下）
borderLeftWidth   : 枠線の太さ（左）
borderRightWidth  : 枠線の太さ（右）
```

枠線の形に関するもの

```text
borderStyle             : 点線、又は実線（solid, dashed, dotted）

borderRadius            : 角の丸み

borderTopLeftRadius     : 角の丸み（左上）
borderTopRightRadius    : 角の丸み（右上）
borderBottomLeftRadius  : 角の丸み（左下）
borderBottomRightRadius : 角の丸み（右下）
```

その他

```text
backfaceVisibility : transform 等で裏返した際に背面が見えるかどうか
backgroundColor    : 背景色の指定
opacity            : 不透明度の指定
```

### 3.3. Text の装飾

```text
color              : 文字色の指定

fontSize           : フォントサイズの指定
fontStyle          : フォントスタイル（普通又は斜体）の指定
fontWeight         : フォントウェイトの指定
fontFamily         : フォントファミリーの指定

lineHieght         : 行の高さの指定
letterSpacing      : 文字間隔の指定
textAlign          : 文字の寄せ方の指定

textDecorationLine : 文字の装飾（打ち消し線、下線等）の指定
textShadowColor    : 文字の影の色の指定
textShadowOffset   : 文字の影のずれ幅の指定
textShadowRadius   : 文字の影の丸みの指定

textTransform      : アルファベットの大文字・小文字変換の指定
```

## 4. React Native Paper（マテリアルデザインテーマ）関連

参考 URL：<https://callstack.github.io/react-native-paper/index.html>（公式ページ）

<!-- TODO: 各コンポーネントのプロパティ等を追記 -->

### 4.1. React Native Paper ライブラリのインストール

```bash
npm install react-native-paper
```

### 4.2. 基本的なテーマの適用

コンポーネントへの適用

```javascript
// babel.config.js
module.exports = function(api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo'],
    env: {
      production: {
        plugins: ['react-native-paper/babel']
      }
    }
  }
}

// App.js
import React from 'react'
import { Provider as PaperProvider } from 'react-native-paper'

export default function App() {
  return (
    <PaperProvider>
      // この範囲に react-native-paper テーマが適用される。
    </PaperProvider>
  )
}
```

### 4.3. テキスト装飾コンポーネント

```text
Headline   : 最も大きい見出し文字
Title      : タイトル。h1 相当
Subheading : h2 相当の見出し文字
Paragraph  : 段落
Caption    : 注釈等に使用できる、薄くて小さい文字
```

### 4.4. アバター表示コンポーネント

```text
アバター（テキスト）
  - Avatar.Text {...props} label='YN'
アバター（アイコン）
  - Avatar.Icon {...props} icon='folder'
```

### 4.5. カード形式表示のコンポーネント

```text
Card.Cover     : カバー画像表示
Card.Title     : 以下の子要素で構成
  - title      : 大きく濃い文字でタイトル
  -subtitle    : 小さく薄い文字でサブタイトル
  -left / right: title/subtitle の左右に配置
Card.Content   : 本文
Card.Actions   : Button 要素を配置し、操作を促す。
```

```javascript
<Card>
  <Card.Cover source={require('../assets/ramen.jpg')} />
  <Card.Title
    title='ラーメン紀行 ２日目'
    subtitle='炎のラーメンちゃんねる'
    left={props => <Avatar.Text {...props} label='YN' />} />
  <Card.Content>
    <Paragraph>とうとうこの伝説のお店にやってきました。</Paragraph>
  </Card.Content>
  <Card.Actions style={{ justifyContent: 'flex-end' }}>
    <Button>見ない</Button>
    <Button mode='contained'>見る</Button>
  </Card.Actions>
</Card>
```

### 4.6. リスト形式で複数データを表示するコンポーネント

```javascript
import React from 'react'
import { Provider as PaperProvider, List } from 'react-native-paper'
import { FlatList } from 'react-native-gesture-handler'
import format from 'date-fns/format'

memos = [
  {text: 'No.1', createdAt: 1585574700000,},
  {text: 'No.2', createdAt: 1585574800000,},
  {text: 'No.3', createdAt: 1585574900000,},
]

export const MainScreen = () => {
  <PaperProvider>
    <FlatList
      style={sytles.list}  // alignItems, justifyContent を指定するとエラー
      data={memos}
      keyExtractor={item => item.createdAt}
      renderItem={({ item }) => (
        <List.Item
          title={item.text}
          titleNumberOfLines={2}  // リストに表示する最大行数。超過分は省略
          description={`Created at: ${format(item.createdAt, 'yyyy.MM.dd HH:mm')}`}
          descriptionStyle={{ textAlign: 'right' }}
        />
      )}
    />
  </PaperProvider>
}
```

### 4.7. Button コンポーネント（React Native Paper）

```javascript
import { Button } from 'react-native-paper';

// ノーマルの Button と異なり、title はタグ範囲内に記述する。
<Button
  mode='contained'
  onPress={onPressButton}
  icon='camera'  // アイコンは省略可
>
  Button_Title
</Button>
```

### 4.8. IconButton コンポーネント

`Button`コンポーネントもアイコンを表示できるが、サイズ変更ができない。

アイコンだけを大きく表示したい場合はこちらを使用する。

```javascript
<IconButton
  icon='trash-can-outline'
  color='white'
  size={40}
  onPress={onPressButton}
  />
```

### 4.9. Switch コンポーネント

設定などで使用する ON/OFF 切り替えスイッチ

なぜか`value`で使用する値が逆になるので注意

以下はスイッチの変更時に自動で設定を保存するサンプル。

`AsyncStorage`は文字列しか保存できない為、
設定を保存する場合は`if`文で`value`値の真偽判定を行なってから文字列を保存する。

```javascript
const save_single_data = async (key, value) => {
  await AsyncStorage.setItem(key, value)
}

const GlobalScreen = () => {
  const [haptics, toggleHaptics] = useState(false)
  const onToggleSwitch = async () => {
    toggleHaptics(!haptics)
    if (!haptics == true) {
      await save_single_data('globalSetting.haptics', 'ON')
      console.log(`[+] Haptics: ON (haptics=${haptics})`)
    }
    else {
      await save_single_data('globalSetting.haptics', 'OFF')
      console.log(`[-] Haptics: OFF (haptics=${haptics})`)
    }
  }

  useEffect(() => {
    get_setting('globalSetting.dark')
      .then((res) => {
        if (res == 'ON') {
          toggleDark(true)
        }
      })
    get_setting('globalSetting.haptics')
      .then((res) => {
        if (res == 'ON') {
          toggleHaptics(true)
        }
      })
  })

  return (
    <View style={{ height: '100%', backgroundColor: '#fff' }}>
      <List.Item
        style={styles.list}
        title='Haptics Feedback'
        titleStyle={{ fontSize: 20, color: 'black' }}
        titleNumberOfLines={2}
        right={props =>
          <Switch value={haptics} onValueChange={onToggleSwitch} />
        }
      />
    </View>
  )
}

```

### 4.10. TextInput コンポーネント（React Native Paper）

```javascript
import React, { useState } from 'react'
import { KeyboardAvoidingView } from 'react-native'
import { TextInput } from 'react-native-paper'

const [ textValue, setText ] = useState('');

// KeyboardAvoidingView を指定する事で、範囲内のビューは画面キーボードに隠れなくなる。
<KeyboardAvoidingView style={styles.container}>
  <TextInput
    style={{ marginBottom: 16 }}  // 入力領域の下部分のマージン指定
    mode='outlined'  // 入力領域の周囲が実線で囲まれる。
    placeholder='Please Input memo.'  // デフォルトで表示されるテキスト
    multiline  // 複数行の入力に対応
    onChangeText={(text) => setText(text)}  // テキストが変更された場合の動作
    // onChangeText で扱う `text` は、このコンポーネントに入力されたテキストを指す。
  />
</KeyboardAvoidingView>
```

### 4.11. 分割線（Divider）コンポーネント

```javascript
import { Divider, Text } from 'react-native-paper'

const Main = () => {
  <View>
    <Text>Lemon</Text>
    <Divider />
    <Text>Mango</Text>
  </View>
}
```

### 4.12. 右下に新規作成画面表示用のボタンを表示（FAB コンポーネント）

```javascript
import React from 'react'
import { Provider as PaperProvider, FAB } from 'react-native-paper'
import { useNavigation } from '@react-navigation/native'

export const MainScreen = () => {
  const navigation = useNavigation()

  const onPressAdd = () => {
    navigation.navigate('Compose')
  }

  <PaperProvider>
    <FAB
      style={{
        position: 'absolute',  // 絶対位置を指定
        right: 16,             // 右から１６
        bottom: 16,            // 下から１６
      }}
      icon='plus'
      onPress={onPressAdd}
    />
    <FAB
      style={{
        position: 'absolute',
        right: 16,
        bottom: 16,
        backgroundColor: 'pink',  // 背景色の指定
      }}
      icon='cog'  // 使用できるアイコンの検索は https://materialdesignicons.com/
      label='Settings'  // アイコンと一緒に表示する文字（表示は大文字になる）
      onPress={onPressAdd}
    />
  </PaperProvider>
}
```

### 4.13. ドロップダウンメニューを表示

`react-native-paper`に加えて、`react-native-paper-dropdown`を使用する。

```bash
npm install react-native-paper-dropdown
```

```javascript
import DropDown from 'react-native-paper-dropdown'

const SettingsScreen = () => {

  const [showDropDown, setShowDropDown] = useState(false)
  const [upto, setUpto] = useState(route.params.upto)
  const dropDownList = [
    { label: '1', value: 1 },
    { label: '2', value: 2 },
    { label: '3', value: 3 },
    { label: '4', value: 4 },
    { label: '5', value: 5 },
    { label: '6', value: 6 },
    { label: '7', value: 7 },
    { label: '8', value: 8 },
    { label: '9', value: 9 },
    { label: '10', value: 10 },
  ]

  return (
    <View>
      <DropDown label='Up to'
        visible={showDropDown}
        showDropDown={() => setShowDropDown(true)}
        onDismiss={() => setShowDropDown(false)}
        value={upto}
        setValue={setUpto}
        list={dropDownList}
      />
      </View>
  )
}
```

## 5. react-native-swipe-list-view ライブラリ

リストのアイテムをスワイプして削除したり、
削除ボタンを表示したりする場合に使用できるライブラリ

### 5.1. インストール

```bash
npm install react-native-swipe-list-view
```

### 5.2. 基本的な使用方法

`Flatlist`などのリストコンポーネントと組み合わせて使用する。

```javascript
  return (
    <View style={styles.container}>
      <SwipeListView
        style={styles.container}
        data={countList}
        keyExtractor={item => item.key}
        // 普段見えている部分
        renderItem={({ item }) => (
          // ここで背景を指定していないと、HiddenItem の色が透過してしまう。
          <View style={{backgroundColor: 'white'}}>
            <List.Item
              style={styles.list}
              left={props => <List.Icon {...props} icon='counter' />}
              title={item.title}
              description={format(item.date, 'yyyy.MM.dd HH:mm')}
              onPress={() => {
                navigation.navigate(
                  'Counter',
                  {
                    key: item.key'
                  })
              }}
            />
          </View>
        )}
        // 普段見えていない部分
        renderHiddenItem={(item, rowMap) => (
          <View style={{ alignItems: 'center', backgroundColor: 'red', flex: 1, flexDirection: 'row', justifyContent: 'flex-end', padingRight: 15}}>
            <IconButton
              icon='trash-can-outline'
              color='white'
              size={40}
              onPress={async () => {
                await delete_single_stored_data(item.item.key)
                initialize()  // 削除してもリストは更新されないので、データロードと state 変更の関数を実行
                // 上位コンポーネントから値を受け取る場合は item.item.key のようになるので注意
                console.log(`[*] Delete Button have touched in No.${item.item.key}.`)
              }} />
          </View>
        )}
        // 左にスワイプした場合、renderItem がどの程度ズレるかの指定
        rightOpenValue={-75}
        // 右へのスワイプを無効化
        disableRightSwipe={true}
        // 省略可：アクションを発火させる左へのスワイプ距離
        rightActivationValue={-500}
        // 省略可：発火するアクション
        onRightActionStatusChange={async (item) => {
          await delete_single_stored_data(item.item.key)
          initialize()
          console.log(`[*] A Swipe action has executed in No.${item.key}.`)
        }}
      />
    </View>
  )
```

## 6. React Navigation（画面遷移）関連

### 6.1. React Navigation ライブラリのインストール

```bash
# コアライブラリインストール
npm install @react-navigation/native

# 依存関係ライブラリインストール
expo install react-native-gesture-handler react-native-reanimated \
             react-native-screens react-native-safe-area-context \
             @react-native-community/masked-view \

#画面遷移の補助ライブラリインストール
npm install @react-navigation/stack
```

### 6.2. 基本的な画面遷移

```javascript
import React from 'react'
import { View, Text, Button } from 'react-native'
import { NavigationContainer, useNavigation } from '@react-navigation/native'
import { createStackNavigator } from '@react-navigation/stack'

function HomeScreen () {
  // navigation は必ず関数内で定義しなければならない。
  const navigation = useNavigation()

  return (
    <View>
      <Text>Home</Text>
      <Button
        title='to detail'
        onPress={() => navigation.navigate('Detail')} />
    </View>
  )
}

function DetailScreen() {
  return (
    <View>
      <Text>Detail</Text>
    </View>
  )
}

// Stack は関数外で定義してＯＫ
const Stack = createStackNavigator()

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName='Home'>
        <Stack.Screen
          name='Home'
          component={HomeScreen}
          options={{ title: 'ホーム' }} />
        <Stack.Screen
          name='Detail'
          component={DetailScreen}
          options={{ title: '詳細設定' }} />
      </Stack.Navigator>
    </NavigationContainer>
  )
}
```

### 6.3. タブによる画面遷移

ライブラリのインストール

```bash
npm install @react-navigation/bottom-tabs
```

基本的なタブによる画面遷移の実装

```javascript
import React from 'react'
import { View, Text } from 'react-native'
import { NavigationContainer } from '@react-navigation/native'
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs'

function Home() {
  return (
    <View>
      <Text>Home Screen.</Text>
    </View>
  )
}

function Settings() {
  return (
    <View>
      <Text>Settings Screen.</Text>
    </View>
  )
}

const Tab = createBottomTabNavigator()

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name='Home' component={Home} />
        <Tab.Screen name='Settings' component={Settings} />
      </Tab.Navigator>
    </NavigationContainer>
  )
}
```

### 6.4. ドロワー（サイドメニュー）による画面遷移

ライブラリのインストール

```bash
npm install @react-navigation/drawer
```

基本的なサイドメニューの実装

```javascript
import React from 'react'
import { View, Text, Button } from 'react-native'
import { NavigationContainer, useNavigation } from '@react-navigation/native'
import { createDrawerNavigator } from '@react-navigation/drawer'

function Home() {
  const navigation = useNavigation()
  return (
    <View>
      <Text>Home Screen.</Text>
      <Button title='Open side-menu' onPress={() => navigation.openDrawer()} />
    </View>
  )
}

function Settings() {
  return (
    <View>
      <Text>Settings Screen.</Text>
    </View>
  )
}

const Drawer = createDrawerNavigator()

export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator>
        <Drawer.Screen name='Home' component={Home}/>
        <Drawer.Screen name='Settings' component={Settings}/>
      </Drawer.Navigator>>
    </NavigationContainer>
  )
}
```

### 6.5. 前の画面に戻る（stack - goBack）

遷移する前に表示していた画面に移動

```javascript
import { useNavigation } from '@react-navigation/native'

const navigation = useNavigation()

const go_back = () => {
  navigation.goBack()
}
// ~~ ~~
<Button onPress={go_back} title='go back' />
```

### 6.6. 遷移先の画面にデータを渡す

データの渡しには、`navigation.navigate`の第２引数に`{key: value}`の形でデータを指定する。

```javascript
import { useNavigation } from '@react-navigation/native'

export const MainScreen = () => {
  const navigation = useNavigation()

  return (
    <View>
      <Button title='goto sub' onPress={() => navigation.navigate('SubScreen', {message: 'Hello!'})} />
    </View>
  )
}
```

データの受取は、`route.params.keyName`で行う。

```javascript
import { useRoute } from '@react-navigation/native'

export const SubScreen = () => {
  const route = useRoute()

  return (
    <View>
      <Text>
        {route.params.message}
      </Text>
    </View>
  )
}
```

## 7. データの永続化関連（async-storage）

### 7.1. 単一データの保存・取り出し

```javascript
import AsyncStorage from '@react-native-async-storage/async-storage'

const key = "entryOne";
const value = "value";

// 簡易保存領域に保存
const set_data = async (key, value) => {
  await AsyncStorage.setItem(key, value)
}

// データの取り出し
const get_single_data = async () => {
  data = await AsyncStorage.getItem('entryOne')
  return data
}
//  ["entryOne","value"]
```

### 7.2. 単一データの削除

```javascript
const remove_data = async (key) => {
  await AsyncStorage.removeItem(key)
}
```

### 7.3. 構造化されたデータの保存

```javascript
const save_data = async (keyNum, title, count) => {
  const key = keyNum
  const date = Date.now()
  const value = JSON.stringify(
    {
      key,   // JSON オブジェクトとして取得する場合、key が消えるので追加
      title,
      count,
      date,
    }
  )
  await AsyncStorage.setItem(key, value)
}
```

### 7.4. 構造化されたデータの取り出し

```javascript
const get_constructed_data = async () => {
  data = await AsyncStorage.getItem('constructedDate')
  //  data = ["1646194719093","{\"key\":\"12345\",\"text\":\"aaaaaa\",\"createdAt\":1646194719093}"],
  return JSON.parse(data[1])
}
```

### 7.5. 全データの取り出し

```javascript
// 全てのエントリーの取り出し
const loadAll = async () => {
  const keys = await AsyncStorage.getAllKeys();  // 保存済みエントリーの全キー値を配列で取得
  keys.sort()  // キー値をソート
  const entryList = await AsyncStorage.multiGet(keys)  // 全キー値の値を取得
  // console.log(JSON.stringify(entryList))
  return entryList.map(entry => JSON.parse(entry[1]))
  // AsyncStorage.setItem で保存した構造化データは次の形になっている。
  //
  // [
  //  ["1646194719093","{\"text\":\"aaaaaa\",\"createdAt\":1646194719093}"],
  //  ["1646199156185","{\"text\":\"bbbb\",\"createdAt\":1646199156185}"]
  // ]
  //
  // よって、JSON.parse(entry[1]) によって、JSON としてパース可能な
  // 配列データの１番目（text, createdAt）のみをパースし、返している。
}
```

### 7.6. 全データの削除

```javascript
const killAll = async () => {
  const keys = await AsyncStorage.getAllKeys()
  keys.map(entry => AsyncStorage.removeItem(entry))
}
```

## 8. デバイスを振動させる

### 8.1. expo-haptics による振動

インストール

```bash
expo install expo-haptics
```

```javascript
import * as Haptics from 'expo-haptics'

// 軽い振動
<Button title='' onPress={() => Haptics.selectionAsync()} />

// 小さい振動
<Button title='' onPress={() => Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success)} />
<Button title='' onPress={() => Haptics.notificationAsync(Haptics.NotificationFeedbackType.Error)} />
<Button title='' onPress={() => Haptics.notificationAsync(Haptics.NotificationFeedbackType.Warning)} />

// 大きい振動
<Button title='' onPress={() => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light)} />
<Button title='' onPress={() => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium)} />
<Button title='' onPress={() => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Heavy)} />
```

## 9. 小技

### 9.1. useState に AsyncStorage.getItem のレスポンスを使用する場合

AsyncStorage の返り値を変数への代入で使用すると`promise`が返ってくる問題の対処

```javascript
  const get_single_data = async (keyNum, arg) => {
    const data = await AsyncStorage.getItem(keyNum)
    return JSON.parse(data)[arg]
  }

  const navigation = useNavigation()
  const route = useRoute()
  const key = route.params.key
  const [title, setTitle] = useState('')
  const [count, setCount] = useState(0)

  useEffect(() => {
    get_single_data(key, 'title').then(setTitle)
    get_single_data(key, 'count').then(setCount)
  }, [])
```

### 9.2. 画面いっぱいにレイヤーを重ねたい場合

全画面タップを仕込む場合などに。

```javascript
export default function App() {
  return (
    <View>
      <Text>テキストはどの順番で記述しても absolute 属性の下に描画される。</Text>
      <FAB  // このボタンはレイヤーの下に描画されてしまうので押せない。
        style={{
          position: 'absolute',
          right: 16,
          bottom: 16,
        }}
        icon='plus'
      />
      <Text style={styles.layer}></Text>
      <FAB  // このボタンはレイヤーの上に描画されるので押せる。
        style={{
          position: 'absolute',
          right: 16,
          bottom: 16,
        }}
        icon='minus'
      />
    </View>
  )
}

const styles = StyleSheet.create ({
  layer: {  // 画面いっぱいに描画透明な Text コンポーネントを描画する。
    width: '100%',
    height: '100%',
    position: 'absolute',
    right: 0,
    bottom: 0,
    alignItems: 'center',
    justifyContent: 'center',
  },
})
```

### 9.3. 遷移元からのデータを useState 内で条件分岐したい場合

遷移元からデータが受け取れるかどうか曖昧な場合、
例えば、新規作成画面と編集画面を兼用するような場合に使用できる。

```javascript
import React, { useState } from 'react'
import { useRoute } from '@react-navigation/native'

export default function App() {
  const route = useRoute()
  const [count, setCount] = useState(() => {
    try {  // 遷移元画面からデータが取得できるかをトライ
      var recieveCount = route.params.number
    }
    catch (e) {
      var recieveCount = 0  // 取得できなかった場合は 0
    }
    return recieveCount  // useState の count の初期値
  })
}
```

## 10. 目的別テンプレート

### 10.1. 永続化データへのデータ保存とリスト生成

```javascript
import React, { useState, useEffect } from 'react'
import { View, Text, StyleSheet } from 'react-native'
import { FlatList } from 'react-native-gesture-handler'
import { Provider as PaperProvider, List, FAB, Divider } from 'react-native-paper'
import { NavigationContainer, useNavigation, useRoute } from '@react-navigation/native'
import { createStackNavigator } from '@react-navigation/stack'
import AsyncStorage from '@react-native-async-storage/async-storage'
import format from 'date-fns/format'

// データ保存用関数
const save_data = async (keyNum, title, text) => {
  const key = keyNum
  const value = JSON.stringify(
    {
      key,
      title,
      text,
      date,
    }
  )
  await AsyncStorage.setItem(key, value)
}

// 特定 key 内から特定キー名の値を取得
const get_single_data = async (keyNum, arg) => {
  const data = await AsyncStorage.getItem(keyNum)
  return JSON.parse(data)[arg]
}

// 全データのロード関数
const loadAll = async () => {
  let keys = await AsyncStorage.getAllKeys()
  const listData = await AsyncStorage.multiGet(keys)
  return await listData.map(entry => JSON.parse(entry[1]))
}

// 特定データの削除関数
const delete_single_stored_data = async (key) => {
  AsyncStorage.removeItem(key)
  console.log(`[!] No.${key} has deleted.`)
}

// Home コンポーネント
const HomeScreen = () => {
  const navigation = useNavigation()
  const [listData, setList] = useState([])

  // 全データをロード、date をキーに降順ソート
  const initialize = async () => {
    const listData = await loadAll()
    listData.sort((a, b) => {
      if (a.date > b.date) return -1
      if (a.date < b.date) return 1
      return 0
    })
    setList(listData)
  }

  useEffect(() => {
    // 画面が遷移先から戻ってきた場合、initialize 関数を実行
    const unsubscribe = navigation.addListener('focus', initialize)
    return unsubscribe
  }, [navigation])

  return (
    <View>
      <FlatList
        data={listData}
        keyExtractor={item => item.key}
        renderItem={({ item }) => (
          <View>
            <List.Item
              title={`${item.title} Last edited: ${format(item.date, 'yyyy.MM.dd HH:mm')}`}
              titleNumberOfLines={1}
              description={item.text}
              description={`Last edited: ${format(item.date, 'yyyy.MM.dd HH:mm')}`}
              descriptionNumberOfLines={1}
              onPress={() => {
                // リストタップで既存データを表示
                // ComposeScreen に渡すのは key のみ。他のデータは遷移先で取得
                navigation.navigate('ComposeScreen',{key: item.key})
              }}
            />
          </View>
        )}
      />
      <FlatList />
      <FAB  // 新規作成画面遷移のボタン。キーは現在時点の日時（UNIX）
        style={{
          position: 'absolute',
          right: 16,
          bottom: 16,
        }}
        icon='plus'
        onPress={() => navigation.navigate(
          'ComposeScreen',
          { key: `${Date.now()}`}
        )}
      />
    </View>
  )
}

// 編集画面
const CounterScreen = () => {
  const navigation = useNavigation()
  const route = useRoute()
  const key = route.params.key
  const [title, setTitle] = useState('New')
  const [count, setCount] = useState(0)
  const [date, setDate] = useState()

  // キーに対応するデータが存在する場合、データをストレージから取得してセット
  useEffect(() => {
    const initialize = async () => {
      get_single_data(key, 'title').then((res) => {
        if (res == undefined) { setTitle('New Counter') }
        else { setTitle(res) }
      })
      get_single_data(key, 'count').then((res) => {
        if (res == undefined) { setCount(0) }
        else { setCount(res) }
      })
    }
    const unsubscribe = navigation.addListener('focus', initialize)
    return unsubscribe
  }, [navigation])

  return (
    <KeyboardAvoidingView>
      <TextInput
        mode='outlined'
        placeholder='Please Input Title.'
        onChangeText={(title) => setTitle(title)}
        value={title}
      />
      <TextInput
        mode='outlined'
        placeholder='Please Input Text.'
        multiline
        onChangeText={(text) => setText(text)}
        value={text}
      />
      <Button  // 上書き保存のボタン
        mode='contained'
        onPress={() => {
          save_data(key, title, text)
          navigation.goBack()
        }}></Button>
    </KeyboardAvoidingView>
  )
}

// react-native-paper と react-navigation の適用
export default function App() {
  return (
    <PaperProvider>
      <NavigationContainer>
        <Stack.Navigator initialRouteName='Home'>
          <Stack.Screen
            name='Home'
            component={HomeScreen}
            options={{
              title: 'Home'
            }}
          />
          <Stack.Screen
            name='Compose'
            component={ComposeScreen}
            options={{
              title: ''
            }}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </PaperProvider>
  )
}
```

## 11. その他記述ルール関連

### 11.1. コメント

```javascript
      // Line Comment
      {/* <Welcome name="Bob" />
          <Text>Block Comment</Text>
      */}
```

### 11.2. 指定可能なカラー名

- aliceblue (`#f0f8ff`)
- antiquewhite (`#faebd7`)
- aqua (`#00ffff`)
- aquamarine (`#7fffd4`)
- azure (`#f0ffff`)
- beige (`#f5f5dc`)
- bisque (`#ffe4c4`)
- black (`#000000`)
- blanchedalmond (`#ffebcd`)
- blue (`#0000ff`)
- blueviolet (`#8a2be2`)
- brown (`#a52a2a`)
- burlywood (`#deb887`)
- cadetblue (`#5f9ea0`)
- chartreuse (`#7fff00`)
- chocolate (`#d2691e`)
- coral (`#ff7f50`)
- cornflowerblue (`#6495ed`)
- cornsilk (`#fff8dc`)
- crimson (`#dc143c`)
- cyan (`#00ffff`)
- darkblue (`#00008b`)
- darkcyan (`#008b8b`)
- darkgoldenrod (`#b8860b`)
- darkgray (`#a9a9a9`)
- darkgreen (`#006400`)
- darkgrey (`#a9a9a9`)
- darkkhaki (`#bdb76b`)
- darkmagenta (`#8b008b`)
- darkolivegreen (`#556b2f`)
- darkorange (`#ff8c00`)
- darkorchid (`#9932cc`)
- darkred (`#8b0000`)
- darksalmon (`#e9967a`)
- darkseagreen (`#8fbc8f`)
- darkslateblue (`#483d8b`)
- darkslategrey (`#2f4f4f`)
- darkturquoise (`#00ced1`)
- darkviolet (`#9400d3`)
- deeppink (`#ff1493`)
- deepskyblue (`#00bfff`)
- dimgray (`#696969`)
- dimgrey (`#696969`)
- dodgerblue (`#1e90ff`)
- firebrick (`#b22222`)
- floralwhite (`#fffaf0`)
- forestgreen (`#228b22`)
- fuchsia (`#ff00ff`)
- gainsboro (`#dcdcdc`)
- ghostwhite (`#f8f8ff`)
- gold (`#ffd700`)
- goldenrod (`#daa520`)
- gray (`#808080`)
- green (`#008000`)
- greenyellow (`#adff2f`)
- grey (`#808080`)
- honeydew (`#f0fff0`)
- hotpink (`#ff69b4`)
- indianred (`#cd5c5c`)
- indigo (`#4b0082`)
- ivory (`#fffff0`)
- khaki (`#f0e68c`)
- lavender (`#e6e6fa`)
- lavenderblush (`#fff0f5`)
- lawngreen (`#7cfc00`)
- lemonchiffon (`#fffacd`)
- lightblue (`#add8e6`)
- lightcoral (`#f08080`)
- lightcyan (`#e0ffff`)
- lightgoldenrodyellow (`#fafad2`)
- lightgray (`#d3d3d3`)
- lightgreen (`#90ee90`)
- lightgrey (`#d3d3d3`)
- lightpink (`#ffb6c1`)
- lightsalmon (`#ffa07a`)
- lightseagreen (`#20b2aa`)
- lightskyblue (`#87cefa`)
- lightslategrey (`#778899`)
- lightsteelblue (`#b0c4de`)
- lightyellow (`#ffffe0`)
- lime (`#00ff00`)
- limegreen (`#32cd32`)
- linen (`#faf0e6`)
- magenta (`#ff00ff`)
- maroon (`#800000`)
- mediumaquamarine (`#66cdaa`)
- mediumblue (`#0000cd`)
- mediumorchid (`#ba55d3`)
- mediumpurple (`#9370db`)
- mediumseagreen (`#3cb371`)
- mediumslateblue (`#7b68ee`)
- mediumspringgreen (`#00fa9a`)
- mediumturquoise (`#48d1cc`)
- mediumvioletred (`#c71585`)
- midnightblue (`#191970`)
- mintcream (`#f5fffa`)
- mistyrose (`#ffe4e1`)
- moccasin (`#ffe4b5`)
- navajowhite (`#ffdead`)
- navy (`#000080`)
- oldlace (`#fdf5e6`)
- olive (`#808000`)
- olivedrab (`#6b8e23`)
- orange (`#ffa500`)
- orangered (`#ff4500`)
- orchid (`#da70d6`)
- palegoldenrod (`#eee8aa`)
- palegreen (`#98fb98`)
- paleturquoise (`#afeeee`)
- palevioletred (`#db7093`)
- papayawhip (`#ffefd5`)
- peachpuff (`#ffdab9`)
- peru (`#cd853f`)
- pink (`#ffc0cb`)
- plum (`#dda0dd`)
- powderblue (`#b0e0e6`)
- purple (`#800080`)
- rebeccapurple (`#663399`)
- red (`#ff0000`)
- rosybrown (`#bc8f8f`)
- royalblue (`#4169e1`)
- saddlebrown (`#8b4513`)
- salmon (`#fa8072`)
- sandybrown (`#f4a460`)
- seagreen (`#2e8b57`)
- seashell (`#fff5ee`)
- sienna (`#a0522d`)
- silver (`#c0c0c0`)
- skyblue (`#87ceeb`)
- slateblue (`#6a5acd`)
- slategray (`#708090`)
- snow (`#fffafa`)
- springgreen (`#00ff7f`)
- steelblue (`#4682b4`)
- tan (`#d2b48c`)
- teal (`#008080`)
- thistle (`#d8bfd8`)
- tomato (`#ff6347`)
- turquoise (`#40e0d0`)
- violet (`#ee82ee`)
- wheat (`#f5deb3`)
- white (`#ffffff`)
- whitesmoke (`#f5f5f5`)
- yellow (`#ffff00`)
- yellowgreen (`#9acd32`)
