interface Item {
    id: string
    name: string
    price: number
}

interface Cart {
    items: Item[]
    total: number
}

function add_to_cart1 (cart: Cart, item: Item) {
    cart.items.push(item)
    cart.total += item.price
}

function add_to_cart2 (cart: Cart, item: Item) {
    return {
        ...cart,
        items: [...cart.items, item],
        total: cart.total + item.price
    }
}

interface UserProfile {
    id: string
    name: string
    lastUpdate: Date
}

interface Player {
    id: string
    score: number
}

const updateUserProfile = (profile: UserProfile, newName: string): void => {
    profile.name = newName
    profile.lastUpdate = new Date()
}

const addScore = (players: Player[], playerId: string, points: number): void => {
    const player = players.find(p => p.id == playerId)
    if (player) {
        player.score += points
    }
}

const updateUserProfilePlus = (profile: UserProfile, newName: string): UserProfile => {
    return {
        ...profile,
        name: newName,
        lastUpdate: new Date()
    }
}

const addScorePlus = (players: Player[], playerId: string, points: number): Player | undefined => {
    const player = players.find(p => p.id == playerId)
    if (player) {
        return {
            ...player,
            score: player.score + points
        }
    }
    else {
        return undefined
    }
}

type Order = { id: number; amount: number; status: 'pending' | 'completed'; userId: number }
const orders: Order[] = [
    { id: 1, amount: 100, status: 'pending', userId: 1 },
    { id: 2, amount: 200, status: 'completed', userId: 2 },
    { id: 3, amount: 50, status: 'completed', userId: 1 }
]

const comp_ord = orders.filter(p => p.status == 'completed')
const sum = comp_ord.reduce()
const sum__with_id = comp_ord.filter(p => p.userId == 1).reduce()