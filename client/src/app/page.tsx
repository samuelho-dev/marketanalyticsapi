import { Redis } from '@upstash/redis';
import styles from './page.module.css';

const redis = Redis.fromEnv();

export const revalidate = 0; // disable cache

export default async function Home() {
  const member = await redis.srandmember<string>('nextjs13');

  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <h1 className={styles.title}>Welcome {member}</h1>
        <p className={styles.description}>
          You have been randomly chosen by the redis algorithm.
        </p>
      </main>
    </div>
  );
}
